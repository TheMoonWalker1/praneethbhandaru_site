var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos - currentScrollPos > 0) {
        document.getElementById("navbar").style.top = "0";
        document.getElementById("content").style.marginTop = "60px";
    } else {
        document.getElementById("navbar").style.top = "-60px";
    }
    if (currentScrollPos == 0) {
        document.getElementById("navbar").style.top = "0";
    }
    console.log(currentScrollPos);
    prevScrollpos = currentScrollPos;
}