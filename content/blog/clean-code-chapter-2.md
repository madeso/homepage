+++
date = "2022-01-23T22:25:03+01:00"
title = "Clean Code - Chapter 2"
+++

## Introduction

Clean Code, mostly authored by [Robert C. Martin, aka Uncle Bob](https://www.getrevue.co/profile/tech-bullshit/issues/tech-bullshit-explained-uncle-bob-830918), has come up lately in discussions and apparently it is still being read. I haven't read it and only read the responses about [how bad it is](https://qntm.org/clean) and I've read that it's pretty popular to hate on it and who am I to miss a trend. Join me as I read chapter to chapter and express my feelings and thoughts about each chapter.  This journey might take a while, I'm a slow reader.

I will call the authors Bob, because it's short, "uncle" is weird and "Robert C. Martin and coauthors" is a bit long. The book is also in the "Robert C. Martin Series" and it says "Robert C. Martin" on the cover so why not let Robert name the "group".

The first chapter is pretty much just interviews with other programmers on their thoughts about what clean code is, in general, so let's jump straight into chapter 2 and my feedback/review.

## Rule 1: Use intention-revealing names.
The first rule is about giving variables names after their intent and that is pretty good. `v` and `theList` are bad names, that I agree with, but `v` might be preferable to a longer name if the intent is clear.

```java
int set_major_version(Version v, int new_major) {
    int old = v.major;
    v.major = new_major;
    return old;
}

int set_major_version(Version version, int new_major) {
    int old = version.major;
    version.major = new_major;
    return old;
}
```

Would you really say that the first version is less clean?

There is also considering code where 'v' might be [the standard name](https://en.wikipedia.org/wiki/UV_mapping) for a certain property:

```java
public class TextureCoordinate
{
    public float u;
    public float v;
}
```


## Rule 2: Avoid disinformation
I don't agree with this rule at all. `hp`, `aix` and `sco` are bad names, that is true, not because of association with "UNIX platforms or variants" as Bob suggests, but because they are not intention-revealing.

`hp` however could could be a good name if you are programming a game, for example, where `hp` has a [commonly understood meaning](https://en.wikipedia.org/wiki/Health_(game_terminology)).
Following the "Bob" logic, a list of `Window` shouldn't be called windows as it could be confused with the operating system from Microsoft, a solar system simulation can't contain the Sun and no more Apple in our nutrition software.

Insanity!

I'll even go as far to claim that NFT is a good name if you are using [Neural Fourier Transforms](https://twitter.com/MegaMileyMakes/status/1452619509601292288) a lot. Just be careful about shortenings and "local" names when speaking to people outside the project.

## Rule 4: Use pronounceable names
Bob thinks we should avoid shortenings and all names should be pronounceable, and I both agree and disagree with this. The shortening of identification to id is commonly understood and this is pronounced I D. Same with CD-ROM. If a phrase or word is used commonly, I don't have a problem with this and if it's used commonly *not* using the shortening is a best noise and at worst confusing for the reader.

*For example*: 

```java
void EnableTransmissionControlProgramInternetProtocol()
{
    // ...
}

void DownloadMotionPictureExpertGroupOneOrTwoAudioLayerThree()
{
    // ...
}
```
Sure they are readable but can you even guess what they do?

```java
void EnableTcpIp()
{
    // ...
}

void DownloadMp3()
{
    // ...
}
```

Which do you prefer? Which names do you think is cleaner? The pronounceable?

This rule is also the first rule to provide a example that breaks other rules. A case could be made that this and all the "fixed" code example only shows this specific rule, but...

If you're writing a book about clean code and rules and presumably want programmers to adopt them, then why provide code that breaks rules in a "fixed" sample. Shouldn't all samples be 100% clean code?

The "fixed" sample provided is the following:

```java
class Customer {
    private Date generationTimestamp;
    private Date modificationTimestamp;;
    private final String recordId = "102";
    /* ... */
}
```
*(That's not a typo on my part, Bob actually has 2 semicolons on one of the rows)*

Using `timestamp` here in a `Date` variable seems to be breaking 2 of the other rules:

1. How is timestamp different from `Date` type *(Rule 12: Don't pun)*
2. Why add the type to the name? *(Rule 6: Avoid encodings)*

## Rule 6: Avoid encodings.
Hurrah. Only 23 pages in and this is the first rule contradiction. I realize this critique might be a little bit weak but I've written it and now you get to read it (or skip it).

> "Adding type or scope information into names simply adds an extra burden of information"

Earlier:

> Not that there is nothing wrong with using prefix conventions like `a` and `the` so long as they make meaningful distinction. For example you might use `a` for all local variables `and` the for all function arguments (footnote: Uncle Bob has stopped doing this in C++)

I general I agree with this but it also depends on the compiler level and language. I recently enabled `Wshadow`, to catch bugs in my code. With this warning enabled a variable isn't allowed to shadow another.

```java
void set_foo(int foo) // warning: foo shadows this.foo
{
    this.foo = foo;
}
```

You can try to come up with a new meaningful name for a variable that isn't tied to the scope but naming is hard.

You can for example add a prefix. Let's use `the_` to distinguish it and fix that warning. We use `the_` here instead of `a_` as we don't want to prefix variables with "argument scope". The obvious question after a while then becomes: Why do some variables have prefixes and not others? I don't consider this code to be clean.

```java
void foobar(int the_foo, int bar)
{
    baz(this.foo, the_foo, bar);
}
```
...so you add the prefix to both

```java
void foobar(int the_foo, int the_bar)
{
    baz(this.foo, the_foo, the_bar);
}
```

and now you have scope information called `the_` that tries to hide that is scope information. How is this clean?


### Rule 6a: Hungarian notation
In this sub chapter Bob only talks about system hungarian, not [apps hungarian](https://en.wikipedia.org/wiki/Hungarian_notation#Systems_Hungarian_vs._Apps_Hungarian). Some argue apps still has meaning, others argue the type system should handle this. The argument against system hungarian is that the compiler should catch it but in a untyped language there isn't any compiler to catch it.

I think it depends on the case (and language) and I think the type system could handle some of it but not all.

*Story time:* In math land there exists points and [vectors](https://en.wikipedia.org/wiki/Euclidean_vector). A point is essentially a vector and vector is usually used to represent it, but the point has a more restricted operation set, you can add two vectors and get a new vector, for example, but you can't add two points and get a new point. Last time I tried to separate points and vectors from in my math library I realized such a system was more complicated than the errors it could mitigate but it couldn't handle everything and the required workarounds could easily sidestep any type safety(a point `P` can also be represented by a vector `V` from origin to `P` and vice versa), so I reverted and added [a note to myself](https://github.com/madeso/euphoria/tree/master/libs/core#warning-about-points-and-vector-classes) if I ever try it again.

That being said there probably aren't many cases where Microsoft hungarian notation could be applied and Bob seems to be in the mindset that this is the only hungarian notation.


### Rule 6b: Member prefixes
Here Bob makes the argument that classes should be small and so there shouldn't be needed to prefix members variables with 'm_' as the IDE will color and/or highlight them to make them distinct.
I agree with the rule but the argument presented against prefixing is not a good one. If you view a diff without a IDE, in a terminal for example, on GitHub or on a different computer you can't rely on your specific IDE settings and his reasoning falls apart.

I think the argument should be closer to something like "the source of a variable should be obvious based on usage, if not, you can prefix with `this.` to make it clear".


### Rule 6c: Interfaces and implementations.
> "You should use I for interface or C for class prefixes, or the Impl post fix."

Hurrah. Another contradiction. Apparently all rules have exceptions and here Bob argues that the `I` prefix is good for interfaces or the `Impl` post fix is good for classes implementing a `I`-less interface. This one break the "Use pronounceable names" rule.

Surprise surprise, I also disagree with this one. In short: Come up with better names! A trick I use is to consider a interface a property and the class something concrete. In practice this usually just ends up to add 'able' to the end: Instead of `IWalk` use `Walkable` or (something that)`CanWalk` and for one of the implementations `WalkableWater` or `WalkingChest`.


## Rule 9: Method names
Bob makes the argument that a method should have a verb or a "verb-phrase". I agree with this, but the authors brushes over a important thing about "getters" and "setters".

IDEs tend to have buttons to [automatically](https://www.jetbrains.com/help/idea/generating-code.html#generate-getters-setters) [adding](https://marketplace.visualstudio.com/items?itemName=afmicc.GetterAndSetterGenerator) [these](https://docs.wholetomato.com/default.asp?W258) and for some it's a [USP](https://en.wikipedia.org/wiki/Unique_selling_proposition). In general, however, I think automatically adding one or both are bad practice and one has to consider what the implications are. They effectively exposes internal state to the users and now that state, or part of it, is public.

For example: What's the difference in encapsulation between these 2 statements?

```java
foo.setBar(foo.getBar() + 1);

foo.bar += 1;
```

My suggestion is to keep the public interface to a minimum and only add getters/setters where and if they are needed.

[Casey Muratori has a great rant](https://www.youtube.com/watch?v=_xLgr6Ng4qQ) about this and he mentions that you should only do it if they do more than getting/setting the property. I think the rant is worth checking out, especially if you, just like I once did, think that making things `private` automatically meant it is encapsulated.


## Rule 12: Don't pun
Bob says:

> Using the same name for 2 different items is essentially a pun.

That is, don't use both `feline` and `cat` in the code base if they refer to the same thing. I 100% agree but disagree on the rule title. Apparently they don't follow their own "good name" rules for the rule titles either. This title breaks their first rule: "Use intention-revealing" names.


## Rule 15: Add meaningful context
I'm saving the best (or worst) for last. Bob has this to say about context.

> There are few names which are meaningful in and of themselves - most are not. Instead you need to place names in context for your reader by enclosing them in well-named classes, functions or namespaces.

I agree with this but the code example presented and its implications are... oh boy...


First, let's start with the "ugly code":

```java
private void printGuessStatistics(char candidate, int count) {
    String number;
    String verb;
    String pluralModifier;
    if (count == 0) {
        number = "no";
        verb = "are";
        pluralModifier = "s";
    } else if (count == 1) {
        number = "1";
        verb = "is";
        pluralModifier = "";
    } else {
        number = Integer.toString(count);
        verb = "are";
        pluralModifier = "s";
    }
    String guessMessage = String.format(
        "There %s %s %s%s", verb, number, candidate, pluralModifier
    );
    print(guessMessage);
}
```

Bob has this to say:

> Do the variables need a more meaningful context? The function names provides only part of the context; the algorithm provides the rest. Once you read through the function you see that the three variables are part of the "guess statistics" message. Unfortunately, the context must be inferred. When you first look at the method, the meaning of the variables are opaque.

Personally I think this code is fine. The "context" for 'number', 'verb' and 'pluralModifier' is 'printGuessStatistics' so I guess they have to do with printing the guess statistics. Bob disagrees and has this to say:

> The function  is a bit too long and the variables are used throughout. To split the function into smaller pieces we need to create a `GuessStatisticsMessage` class and make the three variables fields of this class. This provides a clear context for the three variables. They are definitely part of the `GuessStatisticsMessage`. The improvement of context also allows the algorithm to be made much cleaner by breaking it into many smaller functions."

... so they clean the code up, following all the rules and provide us with the following monstrosity:

```java
public class GuessStatisticsMessage {
    private String number;
    private String verb;
    private String pluralModifier;

    public String make(char candidate, int count) {
        createPluralDependentMessageParts(count);
        return String.format(
            "There %s %s %s%s",
            verb, number, candidate, pluralModifier );
    }

    private void createPluralDependentMessageParts(int count) {
        if (count == 0) {
            thereAreNoLetters();
        } else if (count == 1) {
            thereIsOneLetter();
        } else {
            thereAreManyLetters(count);
        }
    }

    private void thereAreManyLetters(int count) {
        number = Integer.toString(count);
        verb = "are";
        pluralModifier = "s";
    }

    private void thereIsOneLetter() {
        number = "1";
        verb = "is";
        pluralModifier = "";
    }

    private void thereAreNoLetters() {
        number = "no";
        verb = "are";
        pluralModifier = "s";
    }
}
```
Cool. The function that was *too long* had 22 lines and is now converted into a class at 40 lines. Notice any changes?

That's right. The improved code removed the print function, to actually print we need a few more lines, Bob neither mentions of provide it. I guess it's a exercise left to the reader.

```java
private static void printGuessStatistics(char candidate, int count) {
    GuessStatisticsMessage guessMessageMaker = new GuessStatisticsMessage();
    String guessMessage = guessMessageMaker.make(candidate, count);
    print(guessMessage);
}
```

So, when taking into account what the function `printGuessStatistics` does and where a bug might be, one has to now consider twice as many lines.

Oh wait... did I say twice...? Notice that the previously hidden code is now a class that is public. There could be more users of the class. I guess we have to search the code base if we want to make a change to the API of this class. If this class is part of a library, one of the other users could now be external, both within the company and out in the wild. It could accidentally have become a part of the public API and that could be impossible to change. Do you stay true to "clean code" and break both binary and API compatibility or do you make a copy `ImprovedGuessStatisticsMessage`, refactor all of the usage and possibly add a deprecation warning? Tough call and neither option is what I would consider clean.

Compare all of that to how hard it would be to make a change inside a private static function.

Why did the authors even make such a big change. Oh, that's right the context of the variables.

As stated earlier, my stand is that the context for the variables was pretty clear to begin with and moving all local variables to class with a similar name doesn't improve that very much. It might be just me but a function called `printGuessStatistics`  that ends with `print(guessMessage)` is *probably* spending the other part of its body building that message.

But for the sake of the argument, let's assume the context isn't clear enough and see if we can make the context clearer by *not* drastically changing the code.

```java
private void printGuessStatistics(char candidate, int count) {
    // message parts
    String number;
    String verb;
    String pluralModifier;

    // set message parts
    if (count == 0) {
        number = "no";
        verb = "are";
        pluralModifier = "s";
    } else if (count == 1) {
        number = "1";
        verb = "is";
        pluralModifier = "";
    } else {
        number = Integer.toString(count);
        verb = "are";
        pluralModifier = "s";
    }

    // print the message
    String guessMessage = String.format(
        /* Example:
         There are 5 Xs */
        "There %s %s %s%s",
        verb, number, candidate, pluralModifier
    );
    print(guessMessage);
}
```
4 comments and 3 newlines and the function is suddenly a lot cleaner and has 0 mental impact on the rest of the code.

The impact is really something that I think is worth considering as it is another point in favor of the single function solution. Bob and his co-author advocates that the function is too long and a class is needed. Setting aside that the class is public, for a newcomer that starts to use a semi-large code base where this rule has been practiced where does one start? What classes are the "main" ones and what classes are just used once in a private function? Are all the classes for `Foobar` neatly hidden away in a `FoobarUtil` namespace/package? The call stack now is  at least twice as long as most functions only forward to a class that does the "heavy" lifting.
This certainly is manageable but is it really clean code?

I don't care about the downsides, I want a class!

## Small change, big consequence

Before we go there, let's consider how much a change in requirements will affect the code. For the sake of the argument we're going to investigate what changes will need to occur if the customer wants to print a sad smiley if there are no letters for A.

First, `thereAreNoLetters` needs to be aware of the current letter. Let's make it easy and specify in the requirements that we only need a add a sad smiley after "no". The message parts are `createPluralDependentMessageParts`is no longer just dependent on plural but on the character as well, so the function name needs to change.

I said that functions should "be aware" of the candidate and that is kinda hand-wavy. Personally I would add a argument but we will see in the following chapters that Bob likes to add yet another member variable and expose "the argument" to the whole class. Arguments and return values are great, they let us know what a function expects as input and *returns* as result.

Speaking of return values: Note that the `createPluralDependentMessageParts` function actually doesn't return what it "creates" it just sets some member variables. I don't know about you but a function that is called `createSomething` probably should create and return `Something`.

Take note that a earlier rule in this chapter said that "Method names should have verb or verb phrase names" but the authors choose `thereAreManyLetters`, `thereIsOneLetter` and `thereAreNoLetters`. Better names would perhaps be `setupPartsForManyLetters`, `setupPartsForOneLetter` and `setupPartsForNoLetters`. Using `setup` instead of create here also sets the expectation that they don't return anything.

But these functions are only called once so why are they functions, doesn't that just complicate things?

Let's look at the `make` function and how to use it, the part that Bob conveniently left out. To use the class one has to create a instance and call make to get the message string that then can be `print`ed out. Why is make a member function? Does it make any sense to create a object and keep it around for future use?
The answer is no because `make` sets all the member variables. Re using it could potentially lead to thread issues as the function isn't thread safe.


## Making "clean" code clean again

OK... with that out of the way, how could a improved class look?

```java
private static class GuessStatisticsMessage {
    public static void print(char candidate, int count) {
        final GuessStatisticsMessge m = createMessage(count);
        print(String.format(
            "There %s %s %s%s",
            m.verb, m.number, candidate, m.pluralModifier));
        
    }

    private static GuessStatisticsMessage createMessage(int count) {
        switch(count) {
        case 0://                             There are no Xs
            return new GuessStatisticsMessage("are", "no", "s");
        case 1://                             There is 1 X
            return new GuessStatisticsMessage("is", "1", "");
        default://                            There are 5 Xs
            return new GuessStatisticsMessage("are", Integer.toString(count), "s");
        }
    }

    private GuessStatisticsMessage(String verb, String number, String pluralModifier) {
        this.verb = verb;
        this.number = number;
        this.pluralModifier = pluralModifier;
    }

    private String verb;
    private String number;
    private String pluralModifier;
}
```

30 lines.

Change is still harder than the single function, but not by much since all extra functions we introduced are private, even the constructor is private (unlike earlier). The class isn't exposed as it's private static (lives inside another class) and completely replaces the original private static function. The only change we have introduced is all `printGuessStatistics(foo, bar)` needs to be replaced with `GuessStatisticsMessage.print(foo, bar)` and considering they are private static the only user is the current class so no extra files or public classes to browse.

The `Create` function now takes advantage over that there is a class that holds data and all the weird `setup` calls are now just a simple one line constructor call. The mutability of all the variables are now gone. The flow is now much more functional and all "variables" can now all be declared as constants that I guess in Java is called `final`.

Since that class also handles printing there is no need to expose a `make` function, if there ever was a need. In the future if we for some reason need it we can expose it then.


## Conclusion

So, that is the end of chapter 2. Contrary to what it might appear I actually agree with most of the rules but if I had to type up everything I agree with this would be longer and less interesting to read. Most of the rules so far in the book are common sense, but some are wrong and the examples given are sometimes pretty bonkers.

...and so far one could summarize it as "do as I say, not as I do"