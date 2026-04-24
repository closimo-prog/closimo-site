$content = Get-Content -Path index2.html -Raw -Encoding utf8
$pattern = '(?s)var IDB = \[.*?\];'
if ($content -match $pattern) {
    $idb = $matches[0]
    Set-Content -Path data.js -Value $idb -Encoding utf8
    $newContent = $content -replace [regex]::Escape($idb), ''
    # Find the <script> tag where IDB was and insert the source reference
    $newContent = $newContent -replace '<script>', '<script src="data.js"></script><script>'
    Set-Content -Path index2.html -Value $newContent -Encoding utf8
    Write-Host "Successfully extracted IDB to data.js"
} else {
    Write-Error "Could not find IDB array in index2.html"
}
