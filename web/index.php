<?php
ini_set("display_errors", "On");


    $is_upload = false;
    $msg = null;
    if (isset($_POST['submit'])) {
         $temp_file = $_FILES['upload_file']['tmp_name'];
		echo $temp_file;
         $img_path = 'upload/' . $_FILES['upload_file']['name'];
		echo $img_path;
         $bool = move_uploaded_file($temp_file, $img_path);
		if($bool){
		   echo "文件上传成功";
  		}
  		else{
    		echo "文件上传失败";
  		}
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <style>
        body {
            background: #eee;
            padding: 0px;
            margin: 0px;
        }

        h1 {
            background: #0877f7;
            color: white;
            padding: 5px;
            font-variant: small-caps;
            margin-top: 0;
        }

        #content {
            position: relative;
            width: 500px;
            padding: 50px;
            margin: 0 auto;
            background-color: #fff;
            -webkit-box-shadow: 0 0 4px rgba(0, 0, 0, 0.2), inset 0 0 50px rgba(0, 0, 0, 0.1);
            -moz-box-shadow: 0 0 4px rgba(0, 0, 0, 0.2), inset 0 0 50px rgba(0, 0, 0, 0.1);
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2), inset 0 0 50px rgba(0, 0, 0, 0.1);
        }
        #content:before, #content:after {
            position: absolute;
            width: 40%;
            height: 10px;
            content: ' ';
            left: 12px;
            bottom: 12px;
            background: transparent;
            -webkit-transform: skew(-5deg) rotate(-5deg);
            -moz-transform: skew(-5deg) rotate(-5deg);
            -ms-transform: skew(-5deg) rotate(-5deg);
            -o-transform: skew(-5deg) rotate(-5deg);
            transform: skew(-5deg) rotate(-5deg);
            -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            -moz-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
            z-index: -1;
        }
        #content:after {
            left: auto;
            right: 12px;
            -webkit-transform: skew(5deg) rotate(5deg);
            -moz-transform: skew(5deg) rotate(5deg);
            -ms-transform: skew(5deg) rotate(5deg);
            -o-transform: skew(5deg) rotate(5deg);
            transform: skew(5deg) rotate(5deg);
        }
    </style>
    <title>Upload1</title>
</head>
<body>
<h1>File Upload 1</h1>
<div id="content">
<form enctype="multipart/form-data" method="post" action="index.php">
    <p>请选择要上传的图片：<p>
    <input class="input_file" type="file" name="upload_file"/>
    <input class="button" type="submit" name="submit" value="上传"/>
</form>
<?php
    if($msg != null){
        echo "提示：" . $msg;
    }
    if($is_upload){
        echo '<img src="'.$img_path.'" width="250px" />';
    }
?>
<!--Check1: File upload check not secure.-->
<!--Check2: Mime check not secure.-->
</div>
</body>
</html>
