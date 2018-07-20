<!DOCTYPE html>
<html>

<head>
<script>
function changebackgroundColor (){

if (document.body.style.backgroundColor==''){
document.body.style.backgroundColor='blue';}
else if (document.body.style.backgroundColor=='blue')
{document.body.style.backgroundColor='pink';
}else if (document.body.style.backgroundColor=='pink'){document.body.style.backgroundColor='';}}
function turnOnLight(){
document.getElementById("myImage").src="https://www.w3schools.com/js/pic_bulbon.gif"
}
function turnOffLight(){
document.getElementById("myImage").src="https://www.w3schools.com/js/pic_bulboff.gif"
}



</script>

</head>
<!-- in html example -->

<body>

<h2>JavaScript Example</h2>

<button onClick ="turnOnLight()">Turn on light</button>

<img id="myImage" src="https://www.w3schools.com/js/pic_bulboff.gif" style="width:100px">

<!-- inline example -->
<button onClick="turnOffLight()">Turn off the light</button>

<p id='timesOnLabel'>Times On: 0</p>

<button
onClick ='changebackgroundColor()'>Change Background Color</button>

</body>
</html>
