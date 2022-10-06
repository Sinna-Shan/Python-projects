function out(){
    var num1 = parseInt(document.getElementById("num1").value);
    var num2 = parseInt(document.getElementById("num2").value);
    var num3 = parseInt(document.getElementById("num3").value);

    var highest = 0;
    
    if(num1>num2){
        if(num1>num3){
            highest = num1;
        }else{
            highest = num3;
        }   
    }else if(num2>num3){
        highest = num2;
    }else{
        highest = num3;
    }
    var value = highest;
    for(var i=highest;0<highest;i--){
        if (num1%i==0 && num2%i==0 && num3%i==0){
            document.getElementById("HCF").innerHTML = "Higest Common Factor is :" + i;
            break;
        }
    
    while(true){
        if(highest%num1==0 && highest%num2==0 && highest%num3==0){
            document.getElementById("LCM").innerHTML = "Least Common Multiple is :" + highest;
            break;
        }else{
            highest=highest+value;
        }
    }
    }
}