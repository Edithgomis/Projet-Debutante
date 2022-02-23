var randomNumber= Math.floor(Math.random()* 10)+1;
const AffichageHistoryque = document.getElementById('t');
const resultat = document.getElementById('resultat');
const essayer = document.getElementById('essayer');
const b = document.getElementById('b');
var NbreEssai = 1;

function Tester() {
   var NbreUser = Number(essayer.value);
   if (NbreEssai === 1){
       AffichageHistoryque.textContent = 'Vos Tests:';
   }
   AffichageHistoryque.textContent += NbreUser + ' ';
   if (NbreUser === randomNumber)       resultat.textContent = 'Bravo!';
   else if (NbreEssai === 3)           { resultat.textContent = '!!Temps ecouler!! Le bon nombre est :' +randomNumber; b.disabled= true;} 
     else                                resultat.textContent =' Incorrect! Resseyer';
   NbreEssai++;
   essayer.value = '';
   essayer.focus();     

}

   
   

    
