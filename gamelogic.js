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
    

    // Naudojame reguliariąją išraišką, kad išskirtume "Player.x +=" ir "500"
    // var codeplace = document.getElementById("codeplace"); // Gaukite input elementą pagal jo id
    // var tekstas = codeplace.value;
    // var rezultatas = tekstas.match(/(Player\.x \+=) (\d+)/);
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
                // case "s":
                // case "S":
                // case "ArrowDown":
                //     y += 10;
                case "Enter":
                case "ArrowDown":
                var codeplace = document.getElementById("codeplace"); // Gaukite input elementą pagal jo id
                var tekstas = codeplace.value;
                var rezultatas = tekstas.match(/(Player\.x \+=) (\d+)/);

                if (rezultatas) {
                    var skaicius = parseInt(rezultatas[2], 10);
                    skaiciustemp = skaicius
                    xtemp = x
                    function iteracija() {
                        if (x < xtemp + skaicius) {
                            x++;
                            console.log(x); // Čia jūsų veiksmų logika
                            setTimeout(iteracija, 10); // Kviečiame funkciją po 1000 ms (1 sekundės)
                        }
                    }
                    
                    iteracija();
                   
                } else {
                    console.log("Nepavyko rasti atitikimo");
                }
                //     break;
                // case "w":
                // case "W":
                // case "ArrowUp":
                //     y -= 10;
                   
                //     break;
                // case "d":
                // case "D":
                // case "ArrowRight":
                //     x += 3;
                //     break;
                // case "a":
                // case "A":
                // case "ArrowLeft":
                //     x -= 3;
                //     break;
    
                // default:
                //     break;
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