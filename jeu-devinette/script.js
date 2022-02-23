let randomNumber = Math.floor(Math.random() * 10) + 1;
const nombre = document.querySelector('.nombre');
const lastResult = document.querySelector('.lastResult');
const consigne = document.querySelector('.consigne');
const envoyer = document.querySelector('.envoyer');
const entrer= document.querySelector('.entrer');
let nbreCount = 1;
let resetButton;

function tester() {
  let userNbre = Number(entrer.value);
  if (nbreCount === 1) {
    nombre.textContent = 'Vos Testes : ';
  }

  nombre.textContent += userNbre + ' ';

  if (userNbre === randomNumber) {
    lastResult.textContent = 'Bravo!';
    lastResult.style.backgroundColor = 'aquamarine';
    consigne.textContent = '';
    terminerJeux();
  } else if (nbreCount === 3) {
    lastResult.textContent = '!!Temps ecouler!! Le bon nombre est : ' +randomNumber ;
    consigne.textContent = '';
    terminerJeux();
  } else {
    lastResult.textContent = 'Incorrect! Resseyer';
    lastResult.style.backgroundColor = 'red';
      if(userNbre < randomNumber) {
        consigne.textContent = 'Le nombre est trop petit!' ;
    } else if(userNbre > randomNumber) {
        consigne.textContent = 'Le nombre est trop grand  !';
    }
        }

  nbreCount++;
  entrer.value = '';
  entrer.focus();
}

envoyer.addEventListener('click', tester);

function terminerJeux() {
  entrer.disabled = true;
  envoyer.disabled = true;
  resetButton = document.createElement('button');
  resetButton.textContent = 'Faire une nouvelle partie';
  document.body.appendChild(resetButton);
  resetButton.addEventListener('click', recommencer);
  
}

function recommencer() {
  nbreCount = 1;
  const resetParas = document.querySelectorAll('.resultParas p');
  for(let i = 0 ; i < resetParas.length ; i++) {
    resetParas[i].textContent = '';
  }

resetButton.parentNode.removeChild(resetButton);
  entrer.disabled = false;
  envoyer.disabled = false;
  entrer.value = '';
  entrer.focus();
  
  randomNumber = Math.floor(Math.random() * 10) + 1;
}

  