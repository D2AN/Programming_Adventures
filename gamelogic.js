window.addEventListener("load", () => {
    const ekranas = document.getElementById("ekranas");
    const ekranoAukstis = ekranas.clientHeight;
    const ekranoPlotis = ekranas.clientWidth;
    let manoCanvas = document.getElementById("canvas");
    manoCanvas.height = ekranoAukstis;
    manoCanvas.width = ekranoPlotis;
});