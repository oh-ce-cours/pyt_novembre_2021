$i = 0
Do{

    $i++
    Write-Host "crashed, don't worry : i = $i"
    gitautopush.exe . --sleep 5

}Until($i -eq 10000)

Write-Host "Boucle terminée !"