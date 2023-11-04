window.addEventListener("load", () => {

    // ekrano aukstis ir plotis
    const ekranas = document.getElementById("ekranas");
    const ekranoAukstis = ekranas.clientHeight;
    const ekranoPlotis = ekranas.clientWidth;

    let manoCanvas = document.getElementById("canvas");

    padidinkCanvas(manoCanvas, ekranoAukstis, ekranoPlotis);
    console.log("mano canvas?", manoCanvas);

    var ctx = manoCanvas.getContext("2d");
    ctx.beginPath();
    ctx.stroke();

    var kelnes = document.getElementById('kelnes');
    var maike = document.getElementById('maike');
    var oda = document.getElementById('oda');
    var plaukai = document.getElementById('plaukai');
    var veidas = document.getElementById('veidas');
    var kunoaukstis = ekranoAukstis / 5
    var kunoplotis = ekranoAukstis / 10
    var x = 0
    var y = ekranoAukstis - kunoaukstis
    document.addEventListener("keydown", (event) => {
            switch (event.key) {
                case "s":
                case "S":
                case "ArrowDown":
                    y += 10;
                  
                    break;
                case "w":
                case "W":
                case "ArrowUp":
                    y -= 10;
                   
                    break;
                case "d":
                case "D":
                case "ArrowRight":
                    x += 30;
                    break;
                case "a":
                case "A":
                case "ArrowLeft":
                    x -= 30;
                    break;
    
                default:
                    break;
            }
            console.log();
        });

    //ciklas
    function kartojimas() {
        ctx.clearRect(0, 0, manoCanvas.width, manoCanvas.height); // Ištriname seną paveikslėlį
        ctx.drawImage(oda, x, y,kunoplotis,kunoaukstis);
        ctx.drawImage(kelnes, x, y,kunoplotis,kunoaukstis);
        ctx.drawImage(maike, x, y,kunoplotis,kunoaukstis);
        ctx.drawImage(plaukai, x + kunoplotis / 6, y - kunoaukstis/3 ,kunoplotis,kunoaukstis);
        ctx.drawImage(veidas, x + kunoplotis / 6, y - kunoaukstis/3,kunoplotis,kunoaukstis);
     
        requestAnimationFrame(kartojimas);
    }kartojimas();
});
   
//padidinu canvas
function padidinkCanvas(canvasElementas, aukstis, plotis) {
    canvasElementas.height = aukstis;
    canvasElementas.width = plotis;
}

//funkcije kuri išjunge scrolinima
{
    if (document.readyState === 'complete') {
        document.body.style.position = '';
        document.body.style.overflowY = '';

        if (document.body.style.marginTop) {
            const scrollTop = -parseInt(document.body.style.marginTop, 10);
            document.body.style.marginTop = '';
            window.scrollTo(window.pageXOffset, scrollTop);
        }
    } else {
        //window.addEventListener('load', enableBodyScroll);
    }
}

function disableBodyScroll({ savePosition = false } = {}) {
    if (document.readyState === 'complete') {
        if (document.body.scrollHeight > window.innerHeight) {
            if (savePosition) document.body.style.marginTop = `-${window.pageYOffset}px`;
            document.body.style.position = 'fixed';
            document.body.style.overflowY = 'scroll';
        }
    } else {
        window.addEventListener('load', () => disableBodyScroll({ savePosition }));
    }
};