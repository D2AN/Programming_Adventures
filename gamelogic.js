    // 0 = day 1 = night
window.addEventListener("load", () => {

    // ekrano aukstis ir plotis
    const ekranas = document.getElementById("ekranas");
    const ekranoAukstis = ekranas.clientHeight;
    const ekranoPlotis = ekranas.clientWidth;

    let manoCanvas = document.getElementById("canvas");

    padidinkCanvas(manoCanvas, ekranoAukstis, ekranoPlotis);
    console.log("mano canvas?", manoCanvas);
 
    var ctx = manoCanvas.getContext("2d"); 
    ctx.font = '20px Arial';
    ctx.fillStyle = 'black';
    // ctx.beginPath();
    // ctx.stroke();
// var fpsCounter = document.getElementById("fpsCounter");
    var frameCount = 0;
    var fps = 0;

        function updateFPS() {
            console.log(fps + 'fps')

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

    // function circle(x, y, r, c) {
    //     ctx.beginPath();
    //     var rad = ctx.createRadialGradient(x, y, 1, x, y, r);
    //     rad.addColorStop(0, c);
    //     rad.addColorStop(1, 'transparent');
    //     ctx.fillStyle = rad;
    //     ctx.arc(x, y, r, 0, Math.PI*2, false);
    //     ctx.fill();
    // }
    
    // ctx.fillRect(0, 0, 256, 256);
    
    // circle(128, 128, 200, 'red');
    // circle(64, 64, 30,    'green');
    var kelnes = document.getElementById('kelnes');
    var maike = document.getElementById('maike');
    var odaElementas  = document.getElementById('oda');
    var plaukai = document.getElementById('plaukai');
    var veidas = document.getElementById('veidas');
    var debesis1 = document.getElementById('debesis1');
    var saule = document.getElementById('saule');
    var menulis = document.getElementById('menulist');
    var debesis2 = document.getElementById('debesis2');
    var backgraund = document.getElementById('backgraund');
    var backgraundnight = document.getElementById('backgraundnight');
    var BapkesElementas  = document.getElementById('Bapkes');
    var act1  = document.getElementById('act1');
    var act2  = document.getElementById('act2');
    var act3  = document.getElementById('act3');
    var pur  = document.getElementById('pb');
    var tekstasDiv = document.getElementById('tekstas');
    var uzdt = document.getElementById('uzdt');
    var kaip = document.getElementById('kaip');
    var siena = document.getElementById('Siena');
    var BapkesPlotis = BapkesElementas.width;
var BapkesAukstis = BapkesElementas.height;

var odaPlotis = odaElementas.width;
var odaAukstis = odaElementas.height;


// var Bapkes1 = { x: bapx, y: bapy, plotis: BapkesPlotis, aukstis: BapkesAukstis };
// var oda1 = { x: x, y: y, plotis: odaPlotis, aukstis: odaAukstis };
function arSusikerta(objektas1, objektas2) {
    return objektas1.x < objektas2.x + objektas2.plotis &&
           objektas1.x + objektas1.plotis > objektas2.x &&
           objektas1.y < objektas2.y + objektas2.aukstis &&
           objektas1.y + objektas1.aukstis > objektas2.y;
}
    var dankunas = [saule, menulis]
    var backgraundl = [backgraund, backgraundnight]
    var kunoaukstis = ekranoAukstis / 5
    var kunoplotis = ekranoAukstis / 10 + 20
    var x = 200
    var y = ekranoAukstis / 1.5 - kunoaukstis
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
    var sy = ekranoAukstis / 3
    kurisdk = 0
    Inputclear = true
    var lvl = 0
    var gr = 0
    var menu = false
    var bapx = 800
    var bapy = ekranoAukstis / 1.3 - kunoaukstis
    istorija = ['','','']
    var sneka = false
    var sinosaukstis = ekranoAukstis/3

    function snekajis() {
        sneka = true;
        setTimeout(function() {
            sneka = false;
        }, 5000); 
    }

    function tam()
    {
        if(gr < 0.998){gr += 0.01}        
                
    }
    function svie()
    {
        if(gr > 0.01){gr -= 0.01}        
    }
    document.addEventListener("keydown", (event) => {
            switch (event.key) {
                // case "Escape":
                //     if(!menu){document.getElementById('setings').style.visibility = 'visible';
                // menu = true}
                //     else{document.getElementById('setings').style.visibility = 'hidden';
                //         menu = false}

                case "Enter":
                    var codeplace = document.getElementById("codeplace"); // Gaukite input elementą pagal jo id
                    var tekstas = codeplace.value;
                    if (tekstas.trim() !== "") {
                        istorija.unshift(tekstas);
                    }
                    
                    act1.innerText = istorija[0];
                    act2.innerText = istorija[1];
                    act3.innerText = istorija[2];
                    var rezultatas1 = tekstas.match(/(Player\.x \+=) (\d+)/);
                    var rezultatas2 = tekstas.match(/(Player\.x \-=) (\d+)/);
                    var rezultatas3k1 = tekstas.match(/Print\('([^']*)'\)/);
                    var rezultatas3k2 = tekstas.match(/Print\("([^']*)"\)/);
                    if(Inputclear){
                        codeplace.value = "";
                    }
                    xtemp = x
                    xtemp2 = x
                    if (rezultatas1) {
                      var skaicius = parseInt(rezultatas1[2], 10);  
                        
                        
                        function iteracija() {
                            if (xtemp2 < xtemp + skaicius) {
                                x++;
                                xtemp2++;
                                console.log(x); // Čia jūsų veiksmų logika
                                setTimeout(iteracija, 10); // Kviečiame funkciją po 1000 ms (1 sekundės)
                            }
                           
                        }
                        
                    // ifelse(rezultatas2){};   
                        
                    iteracija();
                    } 
                    else if(rezultatas2){
                        var skaicius = parseInt(rezultatas2[2], 10);
                        function iteracija() {if(xtemp2 < xtemp + skaicius){ 
                            x--;
                            xtemp2++;
                            console.log(x); // Čia jūsų veiksmų logika
                            setTimeout(iteracija, 10); // Kviečiame funkciją po 1000 ms (1 sekundės)
                        }}
                        iteracija();
                    }
                    else if(rezultatas3k1){
                            console.log("yra" + rezultatas3k1[1])
                            sako = rezultatas3k1[1]
                            snekajis()
                            tekstasDiv.innerText = sako;
                            burbuloilg = sako.length
                    }
                    else if(rezultatas3k2){
                        console.log("yra" + rezultatas3k2[1])
                        // tekstasDiv.style.top = y - kunoaukstis + 50+'px';
                        // tekstasDiv.style.left = x + kunoplotis + 'px';
                        sako = rezultatas3k2[1]
                        snekajis()
                        tekstasDiv.innerText = sako;
                        burbuloilg = sako.length

                    }
                    else {
                        console.log("Nepavyko rasti atitikimo");
                    }
                    break;
                    case "Shift":
                        Inputclear = !Inputclear;
                        break;
                        
                
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
            
        });

    //ciklas
    function kartojimas() {
        Bapkes1 = { x: bapx, y: bapy, plotis: kunoplotis, aukstis: kunoplotis };
        oda1 = { x: x, y: y, plotis: kunoplotis, aukstis: kunoaukstis };
        var sienas = { x: 600, y: sinosaukstis, plotis: 50, aukstis: ekranoAukstis };
        d12x++ 
        d13x++ 
        d14x++
        d1x++
        d2x += 2 
        d22x += 2 
        d23x += 2 
        d24x += 2
        
        sx += 0.2
        if( sx > ekranoPlotis /2 ){
            sy += ekranoAukstis  / sy / 150
        }
        else{
            sy -= ekranoAukstis / sy / 150  
        }
        // ctx.clearRect(0, 0, manoCanvas.width, manoCanvas.height); // Ištriname seną paveikslėlį 
        tekstasDiv.style.top = y - kunoaukstis + 50+'px';
        tekstasDiv.style.left = x + kunoplotis + 'px';
        ctx.drawImage(backgraundl[0],0,0,ekranoPlotis,ekranoAukstis); 
        ctx.globalAlpha = gr;
        ctx.drawImage(backgraundl[1],0,0,ekranoPlotis,ekranoAukstis);
        ctx.globalAlpha = 1;
        ctx.drawImage(dankunas[kurisdk], sx,sy,100,100);
        ctx.drawImage(debesis1, d1x,d1y + 69);        
        ctx.drawImage(debesis1, d12x,d1y + 72);
        ctx.drawImage(debesis1, d13x,d1y);
        ctx.drawImage(debesis1, d14x,d1y+100);
        ctx.drawImage(debesis2, d2x,d2y+150);
        ctx.drawImage(debesis2, d22x,d2y+120);
        ctx.drawImage(debesis2, d23x,d2y+90);
        ctx.drawImage(debesis2, d24x,d2y+40);
        ctx.drawImage(BapkesElementas , bapx, bapy,kunoplotis,kunoplotis);
        ctx.drawImage(odaElementas, x, y,kunoplotis,kunoaukstis);
        if(sneka){
        ctx.drawImage(pur, x + kunoplotis / 2, y - kunoaukstis,kunoplotis + burbuloilg * 10,kunoaukstis);
        }else{
            sako = ''
            tekstasDiv.innerText = sako;
        }
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
        sy = ekranoAukstis / 3 
        if (kurisdk === 0) {
            kurisdk = 1;
        } else {
            kurisdk = 0;
        }}
        if (sx > ekranoPlotis * 0.9 && kurisdk === 0){
           svie()
        } 
        else if(sx < ekranoPlotis * 0.1 && kurisdk === 1)
        {
            
            tam()
            
        }
        if (sx > ekranoPlotis * 0.9 && kurisdk === 0){
            tam()
         } 
         else if(sx < ekranoPlotis * 0.1 && kurisdk === 0)
         {
             
            svie()
             
         }console.log(gr)
        if(x < 0){
            x = ekranoPlotis - kunoplotis
        }   
        else if(x > ekranoPlotis){
            x = 1
    }
    
    const grd = ctx.createRadialGradient(ekranoPlotis / 2, ekranoAukstis / 2, 0, ekranoPlotis / 2, ekranoAukstis / 2, Math.max(ekranoPlotis, ekranoAukstis));

    grd.addColorStop(0.41,"rgba(255, 255, 255, 0)");
    grd.addColorStop(1,"rgba(7, 54, 180)");
    
    if(lvl === 0){
        uzdt.innerText = "Say Hello World";
        kaip.innerText = `use Print("")`;
        if(sako == 'Hello World'){lvl++}
    }
    else if(lvl === 1){       
        uzdt.innerText = "Take a coin";
        kaip.innerText = "use Player.x += `number`";
        if (arSusikerta(Bapkes1, oda1)) {
            x = 0
            lvl++
            }
    }
    else if(lvl === 2){
        uzdt.innerText = "Take a coin";
        kaip.innerText = "use Player.x -= `number`";
        ctx.drawImage(siena, 600, sinosaukstis,50,ekranoAukstis);
        if (arSusikerta(sienas, oda1)) {
             x -= 3
            }
        if (arSusikerta(Bapkes1, oda1)) {
            x = 0
            lvl++

            }
    }
// Fill with gradient
ctx.fillStyle = grd;
ctx.fillRect(0,0,ekranoPlotis,ekranoAukstis);
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
