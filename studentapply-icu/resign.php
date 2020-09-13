<?php
    $con = mysqli_connect("ip","user","passwd","db");           
    if(mysqli_connect_errno($con)){
        die("erroeeer".mysqli_connect_error());
    }
    mysqli_query($con,"set name utf8");
    $passwd=$_GET["passwd"];
    $name=$_GET["name"];
    $sqlq = "select * from autoresign;";
    $p=0;
    $query=mysqli_query($con,$sqlq);
    while($row = mysqli_fetch_array($query)){
        if($passwd==$row['psswd'] && $name==$row['name']){
            $p=1;
        }
    }
    if($p==0){
        $sql = "insert into autoresign(name,psswd)value('$name','$passwd');";
        mysqli_query($con,$sql);
    }
    mysqli_close($con);
    echo $p;
?>
