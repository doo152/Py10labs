var headOne = document.querySelector("#one");
var headTwo = document.querySelector("#two");
var headOThree = document.querySelector("#three");

headOne.addEventListener("mouseover", function(){
    headOne.textContext = "Mouse Currently OVer";
    headOne.textContent = "red"
})

headTwo.addEventListener("mouseout", function(){
    headTwo.textContent = 'hover over me!';
    headTwo.style.color = 'black'
})
headOThree.addEventListener("dblclick", function(){
    headOThree.textContent ='I was double clicked';
    head0Three.style.color = "Yellow";
})