+++
date = "2022-03-07T20:18:03+01:00"
title = "Clean Code - Chapter 3"
draft = true
+++

The third chapter from Clean Code by [Bob](https://www.getrevue.co/profile/tech-bullshit/issues/tech-bullshit-explained-uncle-bob-830918) is all about function length, return values and arguments. How many arguments should a function take? What does he think about "output arguments" and just how long should a function be?

The red line throughout this chapter is a a [pair of functions from a testing framework](https://github.com/unclebob/fitnesse/blob/3bec390e6f8e9e341149b7d060551a92b93d3154/src/fitnesse/html/HtmlUtil.java#L279-L331) that Bob actually might have written. He is no longer in the top 5 committers to the project but it still "his" repository on GitHub.

Bob has this to say about the code:

> It's hard to find a long function in [FitNesse](https://github.com/unclebob/fitnesse/)(an open-source testing tool), but after a bit of searching I came across this one.

Since this chapter only focuses on the *functions*, both we and Bob will "ignore" the usage of both `PageCrawler` and `PageCrawlerImpl`, the wildcard imports, that `SetupTeardownIncluder` is not a good name and everything else that doesn't relate to the subject of functions.

With that "disclaimer" out of the way, the chapter starts with the following *dirty* code.

```java
public static String testableHtml(PageData pageData) throws Exception
{
    return testableHtml(pageData, false);
}

public static String testableHtml(PageData pageData, boolean includeSuiteSetup)
    throws Exception
{
    WikiPage wikiPage = pageData.getWikiPage();
    StringBuffer buffer = new StringBuffer();
    if(pageData.hasAttribute("Test"))
    {
        if(includeSuiteSetup)
        {
            WikiPage suiteSetup = PageCrawlerImpl.getInheritedPage(
                SuiteResponder.SUITE_SETUP_NAME, wikiPage);
            if(suiteSetup != null)
            {
                WikiPagePath pagePath = suiteSetup.getPageCrawler()
                    .getFullPath(suiteSetup);
                String pagePathName = PathParser.render(pagePath);
                buffer.append("!include -setup .").append(pagePathName).append("\n");
            }
        }
        WikiPage setup = PageCrawlerImpl.getInheritedPage("SetUp", wikiPage);
        if(setup != null)
        {
            WikiPagePath setupPath = wikiPage.getPageCrawler().getFullPath(setup);
            String setupPathName = PathParser.render(setupPath);
            buffer.append("!include -setup .").append(setupPathName).append("\n");
        }
    }
    buffer.append(pageData.getContent());
    if(pageData.hasAttribute("Test"))
    {
        WikiPage teardown = PageCrawlerImpl.getInheritedPage("TearDown", wikiPage);
        if(teardown != null)
        {
            WikiPagePath tearDownPath = wikiPage.getPageCrawler()
                .getFullPath(teardown);
            String tearDownPathName = PathParser.render(tearDownPath);
            buffer.append("\n").append("!include -teardown .").append(tearDownPathName)
                .append("\n");
        }
        if(includeSuiteSetup)
        {
            WikiPage suiteTeardown = PageCrawlerImpl.getInheritedPage(
                SuiteResponder.SUITE_TEARDOWN_NAME, wikiPage);
            if(suiteTeardown != null)
            {
                WikiPagePath pagePath = suiteTeardown.getPageCrawler()
                    .getFullPath(suiteTeardown);
                String pagePathName = PathParser.render(pagePath);
                buffer.append("!include -teardown .").append(pagePathName)
                    .append("\n");
            }
        }
    }
    pageData.setContent(buffer.toString());
    return pageData.getHtml();
}
```

When we have learned all the rules how to write *clean* functions the chapter ends with the following fully refactored *clean* code, following the principles.

```java
package fitnesse.html;

import fitnesse.responders.run.SuiteResponder;
import fitnesse.wiki.*;

public class SetupTeardownIncluder {
    private PageData pageData;
    private boolean isSuite;
    private WikiPage testPage;
    private StringBuffer newPageContent;
    private PageCrawler pageCrawler;


    public static String render(PageData pageData) throws Exception {
        return render(pageData, false);
    }

    public static String render(PageData pageData, boolean isSuite)
        throws Exception {
        return new SetupTeardownIncluder(pageData).render(isSuite);
    }

    private SetupTeardownIncluder(PageData pageData) {
        this.pageData = pageData;
        testPage = pageData.getWikiPage();
        pageCrawler = testPage.getPageCrawler();
        newPageContent = new StringBuffer();
    }

    private String render(boolean isSuite) throws Exception {
        this.isSuite = isSuite;
        if (isTestPage())
            includeSetupAndTeardownPages();
        return pageData.getHtml();
    }

    private boolean isTestPage() throws Exception {
        return pageData.hasAttribute("Test");
    }

    private void includeSetupAndTeardownPages() throws Exception {
        includeSetupPages();
        includePageContent();
        includeTeardownPages();
        updatePageContent();
    }


    private void includeSetupPages() throws Exception {
        if (isSuite)
            includeSuiteSetupPage();
        includeSetupPage();
    }

    private void includeSuiteSetupPage() throws Exception {
        include(SuiteResponder.SUITE_SETUP_NAME, "-setup");
    }

    private void includeSetupPage() throws Exception {
        include("SetUp", "-setup");
    }

    private void includePageContent() throws Exception {
        newPageContent.append(pageData.getContent());
    }

    private void includeTeardownPages() throws Exception {
        includeTeardownPage();
        if (isSuite)
            includeSuiteTeardownPage();
    }

    private void includeTeardownPage() throws Exception {
        include("TearDown", "-teardown");
    }

    private void includeSuiteTeardownPage() throws Exception {
        include(SuiteResponder.SUITE_TEARDOWN_NAME, "-teardown");
    }

    private void updatePageContent() throws Exception {
        pageData.setContent(newPageContent.toString());
    }

    private void include(String pageName, String arg) throws Exception {
        WikiPage inheritedPage = findInheritedPage(pageName);
        if (inheritedPage != null) {
            String pagePathName = getPathNameForPage(inheritedPage);
            buildIncludeDirective(pagePathName, arg);
        }
    }

    private WikiPage findInheritedPage(String pageName) throws Exception {
        return PageCrawlerImpl.getInheritedPage(pageName, testPage);
    }

    private String getPathNameForPage(WikiPage page) throws Exception {
        WikiPagePath pagePath = pageCrawler.getFullPath(page);
        return PathParser.render(pagePath);
    }

    private void buildIncludeDirective(String pagePathName, String arg) {
        newPageContent
            .append("\n!include ")
            .append(arg)
            .append(" .")
            .append(pagePathName)
            .append("\n");
    }
}
```

After being presented with the initial code, Bob gives you a challenge, but I think it's such a good challange I present it after both code pieces.

> Do you understand the function after 3 minutes of study? Probably not.
> There's too much going on in there at too many different levels of abstractions.

Which piece of code is easier to understand and fix? The code that is 53 lines or the code that is 110 lines?

Bob continues with this weird critique of the original code:

> It got lot's of odd strings and many strange and in-obvious data types and APIs.

... but his refactored code doesn't improves anything in that regard. The code still has random strings such as  `"TearDown"`, `"-teardown"` `SuiteResponder.SUITE_TEARDOWN_NAME` and `"-teardown"` and sometimes uses `PageCrawlerImpl` and sometimes `PageCrawler`.

We aren't supposed to care since this is the "Functions" chapter but still Bob complains about how bad the "bad code" is. Here is another log to throw on the fire. Let's all point and laugh at the old code and admire the shiny new *clean* code. Bob is such a *good* programmer.

My [cowboy programming](https://cowboyprogramming.com/2007/01/11/delving-into-cowboy-programming/) mind considers the "before" code to be more readable but let's put common sense away for a minute or two and learn about what Bob considers to be clean code and try to understand why the refactored code is better.

> I massage and refine the code, splitting out functions, changing names, eliminating duplication. I shrink the methods and reorder them. Sometimes I break out whole classes, all while keeping the tests passing. In the end, I wind up with functions that follow the rules I've laid down in this chapter.

Cool. Bob starts out with bad ugly code as well. We're in the same boat. Maybe we can learn the craft and cleanse the bad code from our coding sins. Are you excited? I am. Let's go!

## Functions should be short (at most 4 lines long)

> The first rule of functions is that they should be small. The second rule of functions is that they should be smaller than that.

This is the first thing that Bob brings up so clearly it's the most important. But how small should a function be? In 1999 Bob looked at the source of a program written by Kent Beck:

> Every function in this program was just two, or three, or four lines long. [...] *That's* how short your functions should be!

So Bob looked at some code a while ago where functions were at most 4 lines. Reading further we learn that the source is long lost and only the memory of the code remains. Bob can't justify why functions of max 4 lines are better, they just are.

## Functions should do one thing

The idea that functions should do one thing makes sense in theory, but what exactly is *one thing*? Glad you asked, Bob has also has answers.

> A function does more than one thing if you can extract another function and name it with a name that doesn't restate it's implementation.

This means that:
* `switch` and *long* `if-else` blocks are also *one thing* so they should probably return a interface with a concrete implementation for each branch.
* Blocks within `if`, `else`, `while` statements and so on should probably just be function calls with a "*nice descriptive name*" that "*adds documentary value*".
* Error handling is also *one thing* so you should use exceptions because checking return value is *one thing* and if a function checks the return value for errors then that function does two things and that is not clean.

In a rant, Raymond Chen calls exceptions, [cleaner, more elegant, and wrong](https://devblogs.microsoft.com/oldnewthing/20040422-00/?p=39683) and follows up with that neither he nor that book authors teaching us how to use exceptions are [smart enough to use them](https://devblogs.microsoft.com/oldnewthing/20050114-00/?p=36693). We however are *smart* programmers that write *clean* code. We never introduce any bugs.

Looking at Bob's perfect code it mostly follow this rule that the function should only do *one thing*, but `includeSetupAndTeardownPages` include pages **and** updates the contents of the page. That's two things!

```java
private void includeSetupAndTeardownPages() throws Exception {
    includeSetupPages();
    includePageContent();
    includeTeardownPages();
    updatePageContent();
}
```

As far as I can tell, the reasoning behind this is is that because if he didn't, the render function would increase with 2 more lines and be 6 lines and hence more than 4 lines and that isn't clean. Like this *unclean* code:

```java
private String render(boolean isSuite) throws Exception {
    this.isSuite = isSuite;
    if (isTestPage()) { // changed line
        includeSetupPages(); // new function that only does one thing
        updatePageContent(); // new line
    } // new line
    return pageData.getHtml();
}
```

Gah! It's 6 lines now and *dirty*. We don't want *dirty* code.

## One level of abstraction per function

> We need to make sure that the statements within our function are all at the same level of abstraction. It's easy to see how *the original code* violates this rule. There are concepts in there that are at a very high level of abstraction; others that are at an intermediate level of abstraction; and still others that are remarkably low level.

The original code has different levels of abstractions. That is bad. Let's see how Bob applies this in his refactoring.

```java
private String render(boolean isSuite) throws Exception {
    this.isSuite = isSuite;
    if (isTestPage())
        includeSetupAndTeardownPages();
    return pageData.getHtml();
}
```
Here Bob assigns a member variable (low level) and calls `getHtml()` (high level). Personally I would consider `getHtml()` intermediate and the rest of the calls high level, but Bob explicitly gave `getHtml()` as a example of high level in his example.

I can't see any reason why this clean code that clearly has more than one level of abstraction. From Bobs description it looks *dirty*, but he said that he has followed the rules so it must be some other rule here at play. We might get a better understanding if we keep reading.

## The number of functions arguments

> The ideal number of arguments for a function is zero. Next comes one, followed closely by two.
> One input is the next best thing to no arguments. `SetupTeardownIncluder.render(pageData)` is pretty easy to understand. Clearly we are going to render the data in the `pageData` object.

Let's look again at what all `render(...)` functions do:

```java
public static String render(PageData pageData, boolean isSuite) {
    return new SetupTeardownIncluder(pageData).render(isSuite);
}

private String render(boolean isSuite) {
    this.isSuite = isSuite;
    // ...
}
```

This explains why the constructor only takes one argument and the render member function takes the second. 2 arguments to the constructor would be too confusing.

This also explains why the private `render(boolean)` function assigns a variable and mixes levels of abstractions. Bob had this to say about mixing levels of abstractions:

> Mixing levels of abstraction within a function is always confusing.

Clearly mixing levels of abstractions is less confusing than taking two arguments.

---

> Even obvious two-argument functions like `assertEquals(expected, equals)` are problematic. How many times have you put the `actual` where `expected` should be? The two arguments have no natural ordering. The `expected, actual` ordering is a convention that requires practice to learn.

Personally I never had that the issue with `assertEquals` that Bob has had. Especially if you [follow TDD](https://en.wikipedia.org/wiki/Test-driven_development#Test-driven_development_cycle), [like Bob does](https://twitter.com/unclebobmartin/status/1189574793579941889) and accidentally mix them up, you will see that the `expected` and `actual` values are mixed when you write your initial failing tests.

Looking though the "clean code", what's somewhat confusing is that both `buildIncludeDirective` and `include` both takes two arguments that are strings.

```java
void buildIncludeDirective(String pagePathName, String arg) { /***/ }
void include(String pageName, String arg) { /***/ }
```

It seems they would both have the same problem that the assert function has, and even more so since you don't have a failing test at the start to tell you that you accidentally confused them.

I'm not entirely sure what the `arg` argument is here, but wrapping it in a class would result in a compiler error if they are mixed up. We don't want to program in a [stringly typed language](https://www.youtube.com/watch?v=ZsHMHukIlJY&t=1885s). We have types, why not take advantage of them?

For Bob it doesn't matter if the compiler can catch these issue or not, what matters here is the number of arguments. Except when it does matter...

> In modern languages we have much richer type systems, and the compiler remembers and enforce the types.

---

Moving on, it's apparent that Bob doesn't like functions that take two arguments and to combat the complex expected/equals mix up Bob has a suggestion in the naming function section of this chapter:

> `assertEqeuals` might be better written as `assertExpectedEqualsActual`. This strongly mitigates the problem of having to remember the ordering of the arguments.

So why does he presents us with the `include` function? I guess it's because the order is implied. No need to add extra noise to a function if it's not needed.

```java
private void includeTeardownPage() throws Exception {
    include("TearDown", "-teardown");
}
```
I'm sure Bob never never mixes the argument order to `include`. It's crystal clear that `argument`, sorry `arg`, is `"TearDown"` and `pagePathName` is `"-teardown"`.

A observant reader might notice that encoding the argument names into the function as a solution for mixing up arguments looks really similar to Joel Spolskys argument in [making wrong code look wrong](https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/) for *Apps* Hungarian Notation but as we learned in the earlier chapter Hungarian Notation is not needed when we have types. Encoding types are bad, encoding names is good.


## Use descriptive names

Looking back at the 2 argument functions again...

```java
void buildIncludeDirective(String pagePathName, String arg) { /***/ }
void include(String pageName, String arg) { /***/ }
```

What name is `arg` anyway? I assume it is short for *argument* but I could be wrong. This isn't a name from the original *bad* code. This is a name Bob came up with during the refactoring to the *clean* code. We handled names in the last chapter, so if you forgot about naming, Bob has a refresher in this chapter:

> Don't be afraid to make a name long. A long descriptive name is better than a short enigmatic name. A long descriptive name is better than a long descriptive comment.

Ah, sorry. This refers to function names, not the names of arguments.

Bob said that we should use descriptive names and we shouldn't encode the type in the last chapter but I don't remember if he said anything about argument names being just *argument* so let's just assume `arg` is a good name for the argument and continue learning.

## Argument objects: transforming 2 argument functions to 1 argument

Looking closely at `buildIncludeDirective`.

```java
private void buildIncludeDirective(String pagePathName, String arg) {
    newPageContent
        .append("\n!include ")
        .append(arg)
        .append(" .")
        .append(pagePathName)
        .append("\n");
}
```
It appends both strings to the content in some sort of include/import directive, they seem to go together, shouldn't that be a class?

> When a function seems to need more than two or three arguments, it is likely that some of those arguments ought to be wrapped into a class of their own.

Remember Bobs immortal words:

> Sometimes I break out whole classes. In the end, I wind up with functions that follow the rules I've laid down in this chapter.

Silly me. They don't go together and are totally separate. Otherwise they would probably have been extracted to a class called `IncludeDirectiveBuilder` that would build the include directive so it easily could be added to the page content.

This function is also not *too long*. 6 lines is less than 4, everybody knows that. This is *clean code*. Bob wrote it and Bob is a *clean coder*. I'm sure we won't come back and look at this later.


## Flag arguments

> Flag arguments are ugly. Passing a boolean into a function is a truly terrible practice. It loudly proclaiming that this function does more than one thing.

Bob feels quite strongly about boolean arguments but not enough to refactor the internal `render` functions.

```java
private String render(boolean isSuite) { /***/ }
```

Why is this? Initially I thought it was because Bob was lazy or there was a hidden distinction between the public and private interface, but I think now that Bob talks about magic values, not booleans. It's not a flag argument anymore if the argument comes from from a variable. So functions can take boolean arguments, they just can't 

> I wanted to limit the scope of refactoring to the function and below. Still, the method call `render(true)` is just plain confusing to a poor reader. We should have split the function into two `renderForSuite()` and `renderForSingleTarget()`.

Let's go on a trip down memory lane. Clean Code was released in 2009, the [deprecated annotation](https://docs.oracle.com/javase/7/docs/technotes/guides/javadoc/deprecation/deprecation.html) was released in java 1.5 in 2004, at least 4 years earlier, and according to the documentation:

> Valid reasons to deprecate an API include: It encourages bad coding practices.

Bob could have refactored the public methods and deprecate the old `render` function but for some reason choose not to.

Also take note that he wanted to limit the refactoring, but choose to replace a public interface, possibly a [published interface](https://martinfowler.com/bliki/PublishedInterface.html) forcing all the users of the code to fix compilation issues. Would deprecating or completely removing the flag argument be much different?

It seems when it comes down to it, flag arguments aren't that bad after all.

## (A function should) have no side effects

[Wiktionary](https://en.wiktionary.org/wiki/side_effect) defines side effect as

> Side effect (noun): A change in state caused by a function call

[Wikipedia](https://en.wikipedia.org/wiki/Side_effect_(computer_science)) has *much* more to say

> In computer science, an operation, function or expression is said to have a side effect if it modifies some state variable value(s) outside its local environment, that is to say has an observable effect besides returning a value (the primary effect) to the invoker of the operation. 

Let's look at the functions the the clean code, ordered by their side effects:

```java
///////////////////////////////////////////////////////////////////////////
// public interface: 2
public static String render(PageData pageData) { /***/ }
public static String render(PageData pageData, boolean isSuite) { /***/ }


///////////////////////////////////////////////////////////////////////////
// constructor: 1
private SetupTeardownIncluder(PageData pageData) { /***/ }


///////////////////////////////////////////////////////////////////////////
// accessor: 3

private boolean isTestPage() { /***/ }
private WikiPage findInheritedPage(String pageName) { /***/ }
private String getPathNameForPage(WikiPage page) { /***/ }


///////////////////////////////////////////////////////////////////////////
// directly modifies state: 4

private String render(boolean isSuite) { /***/ }
private void buildIncludeDirective(String pagePathName, String arg) { /***/ }
private void includePageContent() { /***/ }
private void updatePageContent() { /***/ }


///////////////////////////////////////////////////////////////////////////
// indirectly modifies state: 8

private void includeSetupAndTeardownPages() { /***/ }
private void includeSetupPages() { /***/ }
private void includeSetupPage() { /***/ }
private void includeSuiteSetupPage() { /***/ }
private void includeTeardownPages() { /***/ }
private void includeSuiteTeardownPage() { /***/ }
private void includeTeardownPage() { /***/ }
private void include(String pageName, String arg) { /***/ }
```
12 of 15 functions are directly or indirectly modifying state. Out of those 12 functions that modify state, 9 functions take no arguments and return no values, meaning both the input and the output of the algorithm is hidden i.e has side effects.

What do Bob say about side effects?

> Side effects are lies. Your function promises to do one thing, but it also does other hidden things. Sometimes it will make unexpected changes to the variables of its own class. Sometimes it will make them to the parameters passed into the function or to system globals. In either case they are devious and damaging mistruths that often result in strange temporal couplings and order dependencies.

It also seems that there is "temporal coupling and other dependencies" between at least 80% of the functions. For example: What's the difference between `includePageContent` and `updatePageContent`? Looking at the functions side by side, it's impossible to tell.

```java
private void includePageContent() throws Exception {
    newPageContent.append(pageData.getContent());
}

private void updatePageContent() throws Exception {
    pageData.setContent(newPageContent.toString());
}
```
Remember what was said about names in the second chapter?

> Distinguish names in such a way that the reader knows what the differences offer.

Yeah... Bob has also forgotten but look! The functions are only 1 line! Hooray! That's what is most important.

---

"Side effects are lies" Bob exclaims but is this code really 80% lies? Bob also says it clean, so what's going on...?

The only option left is that Bob in his infinite wisdom has invented a new meaning for "side effect" that is different from Wiktionary, Wikipedia and everyone else's definition. Let's read the text more carefully:

> If you must have temporal coupling, you should make it clear in the name of the function. In this case we might rename the function `checkPasswordAndIntiializeSession`, though that certainly violates "Do one thing".

Ah, now it's clear.

Side effects is when a function does more than one thing but doesn't mention in the function name that it does two things. This must be what Bob means when he says "side effects". It's not sneakily mutating state like the common definition suggest, that everybody else uses, but that the function does more than one thing behind our backs.

Like this `includeSetupAndTeardownPages` that both includes pages **and** updates the page content:

```java
private void includeSetupAndTeardownPages() throws Exception {
    includeSetupPages();
    includePageContent();
    includeTeardownPages();
    updatePageContent();
}
```

...and `buildIncludeDirective` that both builds the include directive **and** appends the directive to the page content.

```java
private void buildIncludeDirective(String pagePathName, String arg) {
    newPageContent
        .append("\n!include ")
        .append(arg)
        .append(" .")
        .append(pagePathName)
        .append("\n");
}
```

> In  the end I wind up with functions that follow the rules I've laid down in this chapter. 

Lies.


## Output arguments

If you needed more examples on Bobs position on sneakily modify state and side effects, you have come to the right place.

> Arguments are most naturally interpreted as *inputs* to a function. If you have been programming for more than a few years, I'm sure you've done a double-take on a argument that was actually an *output* rather than a input.

Ah, good.

> Much of the need for output arguments disappears in object oriented languages because `this` is *intended* to act as an output argument.

That's right Bob. You tell them! Real programmers discards regular return values, immutable values, tuples and classes. Forget about thinking about objects and functions that can be applied to them. This is the real reason why object oriented languages was created!

Who needs return values when we have a license to promiscuously modify the state of the object?




## Output arguments continued

> I'm sure you've done a double-take on an argument that was actually an output rather than an input. For example: `appendFooter(s);`
> [...] Is `s` an input or an output?.
>
> `public void appendFooter(StringBuffer report)`
> 
> This clarifies the issue, but only at the expense of checking the declaration of the function.

Hey Bob, I'm not sure that this clarifies anything at all. In case you didn't know, `StringBuffer` is class and classes are passed as a reference and you need to look at the implementation to know what a function does.

`appendFooter` can be implemented in 2 ways:

```java
public void appendFooter(StringBuffer b)
{
    b.apend("footer");
}

public void appendFooter(StringBuffer b)
{
    page.append(b.toString());
}
```



## Conclusion

Let's end with a quote where Bob talks about a quote from from Ward Cunningham from the first chapter where Bob tries to figure out what clean code is. This quote is so important that Bob also restates it in this 3rd chapter:

> Remember [Ward](https://en.wikipedia.org/wiki/Ward_Cunningham)'s principle, "You know you are working on clean code when each routine you read turns out to be pretty much what you expected".
> Statements like this are characteristic of Ward. You read it, nod your head, and the go on to the next topic. It sounds so reasonable, so obvious, that it barely registers as something profound.

and then he presents this as clean code...

```java
private String render(boolean isSuite) throws Exception {
    this.isSuite = isSuite;
    if (isTestPage())
        includeSetupAndTeardownPages();
    return pageData.getHtml();
}
```

1. Where is `isSuite` used? Why do we even assign it?
2. When is `pageData` updated? I would assume it is inside `includeSetupAndTeardownPages`?
3. If `includeSetupAndTeardownPages` is modifying the `pageData`, can we assume `isTestPage` doesn't?

... and that is just scratching the surface. Not a single line in this functions is what I expect. Looking at each function in isolation and at the surface they look "clean" but it's only clean because all the mess is swept under the rug.

I guess clean code is clean but it's not what I consider clean.
