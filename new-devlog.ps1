$filename = "$(Get-Date -Format 'yyyy')-$(Get-Date -UFormat '%V').md"
# Write-Output $filename
hugo new "devlog/$filename"
