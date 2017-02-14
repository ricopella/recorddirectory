/ ---- nav bar ---- /

function myFunction() {
    var x = document.getElementById("navigation");
    if (x.className === "topNav") {
        x.className += " responsive";
    } else {
        x.className = "topNav";
    }
}