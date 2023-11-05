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
    var fpsCounter = document.getElementById("fpsCounter");
    var frameCount = 0;
    var fps = 0;

        function updateFPS() {
            fpsCounter.innerHTML = "FPS: " + fps;

            // Nustatome FPS skaičių į pradinę reikšmę
            fps = frameCount;

            // Nustatome kadrų skaičių į pradinę reikšmę
            frameCount = 0;
        }

        // Pradiniuose nustatymuose mes rodydami FPS nustatomas 0
        updateFPS();
    function calculateFPS() {
        frameCount++;
        requestAnimationFrame(calculateFPS);
    }

    // Pradėkite skaičiuoti FPS
    calculateFPS();
    setInterval(updateFPS, 1000);
    // Naudojame reguliariąją išraišką, kad išskirtume "Player.x +=" ir "500"
    // var codeplace = document.getElementById("codeplace"); // Gaukite input elementą pagal jo id
    // var tekstas = codeplace.value;
    // var rezultatas = tekstas.match(/(Player\.x \+=) (\d+)/);
    var kelnes = document.getElementById('kelnes');
    var maike = document.getElementById('maike');
    var oda = document.getElementById('oda');
    var plaukai = document.getElementById('plaukai');
    var veidas = document.getElementById('veidas');
    var debesis1 = document.getElementById('debesis1');
    var saule = document.getElementById('saule');
    var menulis = document.getElementById('menulist');
    var debesis2 = document.getElementById('debesis2');
    var backgraund = document.getElementById('backgraund');
    var backgraundnight = document.getElementById('backgraundnight');
    var dankunas = [saule, menulis]
    var backgraundl = [backgraund, backgraundnight]
    var kunoaukstis = ekranoAukstis / 5
    var kunoplotis = ekranoAukstis / 10
    var x = 0
    var y = ekranoAukstis - kunoaukstis
    var d12x = 375   
    var d13x = 598
    var d14x = 243
    var d22x = 721
    var d23x = 134
    var d24x = 907
    var d2x = 429
    var d2y = 0
    var d1y = 0
    var d1x = 811
    var sx = 0
    var sy = ekranoAukstis / 2 
    kurisdk = 0
    Inputclear = true
    document.addEventListener("keydown", (event) => {
            switch (event.key) {
                // case "s":
                // case "S":
                // case "ArrowDown":
                //     y += 10;
                case "Enter":
                    var codeplace = document.getElementById("codeplace"); // Gaukite input elementą pagal jo id
                    var tekstas = codeplace.value;
                    var rezultatas1 = tekstas.match(/(Player\.x \+=) (\d+)/);
                    var rezultatas1 = tekstas.match(/(Player\.x \+=) (\d+)/);
                    if(Inputclear){codeplace.value = "";}
                    if (rezultatas1) {
                        var skaicius = parseInt(rezultatas1[2], 10);
                        
                        skaiciustemp = skaicius
                        xtemp = x
                        function iteracija() {
                            if (x < xtemp + skaicius) {
                                x++;
                                console.log(x); // Čia jūsų veiksmų logika
                                setTimeout(iteracija, 10); // Kviečiame funkciją po 1000 ms (1 sekundės)
                            }
                        }
                    // ifelse(rezultatas2){};   
                        iteracija();
                    
                    } else {
                        console.log("Nepavyko rasti atitikimo");
                    }
                    break;
                case "*" && "/":
                    Inputclear = !Inputclear;
                    break;

                    
                case "w":
                case "W":
                case "ArrowUp":
                    y -= 10;
                   
                    break;
                case "d":
                case "D":
                case "ArrowRight":
                    x += 3;
                    break;
                case "a":
                case "A":
                case "ArrowLeft":
                    x -= 3;
                    break;
    
                default:
                    break;
            }
            console.log();
        });

    //ciklas
    function kartojimas() {
       
        d12x++ 
        d13x++ 
        d14x++
        d1x++
        d2x += 2 
        d22x += 2 
        d23x += 2 
        d24x += 2
        sx++
        if(sy > 30 && sx < ekranoPlotis / 2){sy -= 0.4}
        else{sy += 0.4}
        ctx.clearRect(0, 0, manoCanvas.width, manoCanvas.height); // Ištriname seną paveikslėlį 
        ctx.drawImage(backgraundl[kurisdk],0,0,ekranoPlotis,ekranoAukstis);
        ctx.drawImage(dankunas[kurisdk], sx,sy);
        ctx.drawImage(debesis1, d1x,d1y + 69);        
        ctx.drawImage(debesis1, d12x,d1y + 72);
        ctx.drawImage(debesis1, d13x,d1y);
        ctx.drawImage(debesis1, d14x,d1y+100);
        ctx.drawImage(debesis2, d2x,d2y+150);
        ctx.drawImage(debesis2, d22x,d2y+120);
        ctx.drawImage(debesis2, d23x,d2y+90);
        ctx.drawImage(debesis2, d24x,d2y+40);
        
        ctx.drawImage(oda, x, y,kunoplotis,kunoaukstis);
        ctx.drawImage(kelnes, x, y,kunoplotis,kunoaukstis);
        ctx.drawImage(maike, x, y,kunoplotis,kunoaukstis);
        ctx.drawImage(plaukai, x + kunoplotis / 6, y - kunoaukstis/3 ,kunoplotis,kunoaukstis);
        ctx.drawImage(veidas, x + kunoplotis / 6, y - kunoaukstis/3,kunoplotis,kunoaukstis);
       if(d1x > ekranoPlotis){d1x = -100}
       if(d2x > ekranoPlotis){d2x = -100}
       if(d12x > ekranoPlotis){d12x = -100}
       if(d22x > ekranoPlotis){d22x = -100}
       if(d13x > ekranoPlotis){d13x = -100}
       if(d23x > ekranoPlotis){d23x = -100}
       if(d14x > ekranoPlotis){d14x = -100}
       if(d24x > ekranoPlotis){d24x = -100}
       if(sx > ekranoPlotis){
        sx = 0 
        if (kurisdk === 0) {
            kurisdk = 1;
        } else {
            kurisdk = 0;
        }}
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