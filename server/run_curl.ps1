$baseUrl = "http://localhost:8000"

function Run-Log {
    param($file, $cmdArgs, $display)
    echo $display > $file
    cmd /c curl $cmdArgs >> $file
}

Run-Log "loginuser" "-X POST -H ""Content-Type: application/json"" -d ""{\""userName\"":\""user\"", \""password\"":\""password123\""}"" -c cookies.txt $baseUrl/login/" "curl -X POST -H ""Content-Type: application/json"" -d ""{\""userName\"":\""user\"", \""password\"":\""password123\""}"" -c cookies.txt $baseUrl/login/"

Run-Log "logoutuser" "-X POST -b cookies.txt $baseUrl/logout/" "curl -X POST -b cookies.txt $baseUrl/logout/"

Run-Log "getdealerreviews" "$baseUrl/reviews/dealer/1" "curl $baseUrl/reviews/dealer/1"

Run-Log "getalldealers" "$baseUrl/get_dealers/" "curl $baseUrl/get_dealers/"

Run-Log "getdealerbyid" "$baseUrl/dealer/1" "curl $baseUrl/dealer/1"

Run-Log "getdealersbyState" "$baseUrl/get_dealers/Kansas" "curl $baseUrl/get_dealers/Kansas"

Run-Log "getallcarmakes" "$baseUrl/get_cars/" "curl $baseUrl/get_cars/"
