<?php
    $con = mysqli_connect("ip","user","passwd","db");           
    if(mysqli_connect_errno($con)){
        die("erroeeer".mysqli_connect_error());
    }
    mysqli_query($con,"set name utf8");
    $sql = "select * from applyboard";

    $query = mysqli_query($con,$sql);
    $passwd=$_GET["passwd"];
    $name=$_GET["name"];
    $p=0;
    while($row = mysqli_fetch_array($query)){
        if($passwd==$row['passwd'] && $name==$row['name']){
            $p = 1;
            $times = $row['times']+1;
            $sql1 = "update applyboard set times=".$times." where passwd=".$passwd;
            mysqli_query($con,$sql1);
        }
    }
    mysqli_close($con);
    echo $p;
?>
