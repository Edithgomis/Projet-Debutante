
onload= init
 var lamp = true
function init() {
    document.getElementById("bt").onclick=journuit
    document.getElementById("photo").onclick=journuit
    journuit()
    
}
function jour( ){
    document.getElementById("bt").value="Off"
    document.getElementById("photo").src="on.gif" 
    document.body.style.background = '#FFFFE0'
    document.querySelector('h1').style.color = '#000000'
    
    document.querySelector('h1').style.fontSize = '50px'
}
function nuit( ){
    document.getElementById("bt").value="On"
    document.getElementById("photo").src="off.gif"
    document.body.style.background = '#000000'
    document.querySelector('h1').style.color = '#ffffff'
    document.querySelector('h1').style.fontSize = '50px'
    
}
function journuit(){
    if(lamp==true){jour()
        lamp=false

    }else{
        nuit()
        lamp=true
    }
}