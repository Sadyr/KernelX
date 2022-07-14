/* Значение из текстовых инпутов*/



function check() {
    let x = document.getElementById("mySelect").value;
    if(x === "IP"){
       document.getElementById("demo").innerHTML =  "jjvjrv" ;
    }
    if(x !=  "IP"){
        document.getElementById("demo").innerHTML = "nnn" ;
     }
}






const totalCost = document.getElementById('total-cost'),
      creditTerm = document.getElementById('credit-term'),
      totalCostCf = document.getElementById('total-cost-cf'),
      creditTermCf = document.getElementById('credit-term-cf');

/* Значение из range инпутов*/

const totalCostRange = document.getElementById('total-cost-range'),
      creditTermRange = document.getElementById('credit-term-range'),
      totalCostRangeCf = document.getElementById('total-cost-range-cf'),
      creditTermRangeCf = document.getElementById('credit-term-range-cf');


/* Итоговые значения*/
const totalAmountOfCredit = document.getElementById('amount-of-credit'),
      totalPercent = document.getElementById('percent'),
      totalMonthlyPayment = document.getElementById('monthly-payment');
      
totalPercent.innerHTML = 6 + ' %';

/* Все range: */
const inputsRange = document.querySelectorAll('.input-range');

/* Все input number: */
const inputsNumber = document.querySelectorAll('.input-number');






const assignValue = () => {
    totalCost.value = totalCostRange.value;
    creditTerm.value = creditTermRange.value;
}

assignValue();

const assignValueRange = () => {
    totalCostRange.value = totalCost.value;
    creditTermRange.value = creditTerm.value;
}

assignValueRange();

const assignValueCf = () => {
    totalCostCf.value = totalCostRangeCf.value;
    creditTermCf.value = creditTermRangeCf.value;
}

assignValueCf();

const assignValueCfRange = () => {
    totalCostRangeCf.value= totalCostCf.value ;
    creditTermRangeCf.value = creditTermCf.value ;
}

assignValueCfRange();




const percent = 6;


for(let input of inputsRange){
    input.addEventListener('input', () => {
      assignValue(); 
      assignValueRange();
      assignValueCf();
     assignValueCfRange();
    
      calculation(totalCost.value,percent,creditTerm.value);   
    })
}

for(let input of inputsNumber){
    input.addEventListener('input', () => {
      assignValueRange();
      assignValue(); 
      assignValueCf();
      assignValueCfRange();
   
      calculation(totalCost.value,percent,creditTerm.value);   
    })
}








const calculation = (totalCost = 0,creditTerm = 1,percent = 6) =>{
/*
    ЕП - Ежемесячный платеж
    РК - Размер кредита
    ПС - Процентная ставка
    КМ - Количество месяцев

    ЕП = (РК + (((РК / 100) * ПС) / 12) * КМ) / КМ
*/
    let monthlyPayment; // Ужемесячный платеж
    let lounAmount = totalCost //Размер кредита
    let interestRate = percent; //Процентная ставка
    let numberOfMonths = creditTerm; //Количество месяцев

    monthlyPayment = percent  + lounAmount + interestRate*numberOfMonths;
    if (monthlyPayment < 0){
        return false;
    } else {
        totalAmountOfCredit.innerHTML = lounAmount + '<span>₸</span>';
        totalMonthlyPayment.innerHTML = monthlyPayment + '<span>₸</span>';
        

    }
    //console.log(monthlyPaymentArounded);
}

