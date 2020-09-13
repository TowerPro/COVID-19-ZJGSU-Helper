<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width,initial-scale=1,user-scalable=0"/>
    <title>温馨提示</title>
    <link rel="stylesheet" href="https://students.demoo.com.cn/htmlstatic/plug/weuix/css/weui.css"/>
    <link rel="stylesheet" href="https://students.demoo.com.cn/htmlstatic/plug/weuix/css/weuix.css"/>
    <link rel="stylesheet" href="https://students.demoo.com.cn/htmlstatic/plug/weuix/css/common.css"/>
    <script src="https://students.demoo.com.cn/htmlstatic/plug/jquery2.1.4/jquery.min.js"></script>
    <script src="https://students.demoo.com.cn/htmlstatic/plug/jquery.validate.min.js"></script>
    <script src="https://students.demoo.com.cn/htmlstatic/plug/jquery.form.min.js"></script>
    <script src="https://students.demoo.com.cn/htmlstatic/plug/weuix/js/zepto.min.js"></script>
    <script src="https://students.demoo.com.cn/htmlstatic/plug/weuix/js/zepto.weui.js"></script>
    <script src="https://students.demoo.com.cn/htmlstatic/plug/weuix/js/php.js"></script>
    <script src="https://students.demoo.com.cn/htmlstatic/plug/weuix/js/picker.city.js"></script>
</head>
<body>
<div id="popout"></div>
<div id="mask"></div>
<div id="navigation"></div>
<div id="content">   
     <style>
        .weui-pay-m::before {
            content: none;
        }
    </style>
    <div class="weui-tab" style="height:auto;">
        <div>
            <img style="width: 100%" src="https://hzdemoo.oss-cn-hangzhou.aliyuncs.com/zjgsu/1592876109703.png" alt="">
        </div>
        <div>
            <?php
                $con = mysqli_connect("ip","user","passwd","db");           
                if(mysqli_connect_errno($con)){
                    die("erroeeer".mysqli_connect_error());
                }
                $t=$_GET['t'];
                mysqli_query($con,"set name utf8");
                $sql = "select * from libnum order by time desc limit 1;";
                $query = mysqli_query($con,$sql);
                while($row = mysqli_fetch_array($query)){
                    $time = $row['time'];
                    $number = $row['number'];
                }
                if($time < "07:00:00"){
                    $word = "现在才".$time.",再睡一会儿吧！";
                }
                elseif($time > "20:30:00"){
                    $word = $time."是不能预约入馆的时间，那就出去玩或者回寝室吧！";
                }
                else {
                    if($number=='0'){
                        $word = "居然被预约完了，去字母楼读书吧！";
                    }
                    else {
                        $word = "现在是".$time.",图书馆里还能预约".$number."个位子，快去读书吧！";
                    }
                }
                echo "<h2 align='center' style='color:orangered;'>$word</h2>";
                mysqli_close($con);
            ?>
            <p>&nbsp;</p>
            <h2 align="center">Update 12/09/2020</h2>
            <h3 align="center" style="color:cadetblue;">自动打卡上线，欢迎后台提交表单。</h3>
            <h2 align="center">Update 11/09/2020</h2>
            <h3 align="center" style="color: cadetblue;">自动打卡暂时无法使用，敬请期待。</h3>
            <h3 align="center" style="color: cadetblue;">非必要情况请使用正版出校码，请小心使用。</h3>            
            <p>&nbsp;</p>
            <h4 align="auto" style="color: orangered;">&nbsp;&nbsp;&nbsp;&nbsp;"【保卫处重要通报】近期保卫处发现有部分同学购买或是通过其他渠道使用非法的假入校码进出校园，该入校码据说是某学院学生开发制作，仿真度极高，请各学院通知学生绝不可再使用，更不能将链接透漏给校外人员，保卫处加大识别力度，一旦查实将通报学院协查!"</h4>
            <div class="weui-btn-area">
                <button  class="weui-btn weui-btn_primary" id="btn">我已知晓，由于情况特殊急需出校/入校</button>
                <button class="weui-btn weui-btn_primary" id='btn_a'>云战疫自动打卡申请</button>
            </div>
            <script>
                $(function(){
                    $("#btn").on("click",function(){
                        jump1();
                    });
                    $("#btn_a").on("click",function(){
                        jump2();
                    });
                });
                function jump1(){
                    url = "login.html";
                    window.location.href = url;
                }
                function jump2(){
                    url = "autoresign.html";
                    window.location.href = url;
                }

            </script>
        </div>
        <div class="weui-footer" style="margin-top: 30px">
            <p class="weui-footer__text">浙江工商大学学生处<br>
                Copyright 2018-2020 <br></p>
        </div>
    </div>


</div>
</body>
</html>
