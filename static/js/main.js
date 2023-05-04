$('#pasport').mask('99-99 999999');
$('#inn').mask('999999999999');
$('#snils').mask('999-999-999 99');

function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

async function trainForm(event) {
    event.preventDefault();
    let formData = new FormData(event.target);
    formData.append("expenses", Number(formData.get("expenses1")) + Number(formData.get("expenses2")) + Number(formData.get("expenses3")) + Number(formData.get("expenses4")))
    let response = await fetch(`${window.location.origin}/api/v1/trained-model/check/`, {
            method: 'POST',
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: formData
        }
    );
    let result = await response.json();
    console.log(result);
    let mywindow = window.open('', 'PRINT');

    mywindow.document.write(`<html><head><title>Документ</title>`);
    mywindow.document.write('</head><body >');
    mywindow.document.write(
        `<h1>${result.result ? "Вам одобрен кредит" : "Вам не одобрен кредит"}</h1>
         <h2>Данные по запросу заявителя:</h2>
         <h4>Паспорт заявителя: ${result.pasport}</h4>
         <h4>ИНН заявителя: ${result.inn}</h4>
         <h4>Снилс заявителя: ${result.snils}</h4>
         <h4>Общий доход: ${result.income}</h4>
         <h4>Общий расход: ${result.expenses}</h4>
         <h4>Разница между доходом и расходом: ${Number(result.income) - Number(result.expenses)}</h4>
         <h4>Заработная плата: ${result.salary}</h4>
         <h4>Заработная плата супруги(а): ${result.spouse_salary}</h4>
         <h2>Информация по кредиту:</h2>
         <h4>Процентная ставка кредита: ${result.interest_rate}</h4>
         <h4>Запрашиваемая сумма кредита: ${result.loan_amount}</h4>
         <h4>Срок запрашиваемого кредита (в годах): ${result.loan_term} </h4>
         <h4>Ежемесячная плата: ${result.monthly_payment} </h4>
         <h4>Общая сумма кредита: ${result.main_sum} </h4>`
    );
    mywindow.document.write('</body></html>');

    mywindow.document.close(); // necessary for IE >= 10
    mywindow.focus(); // necessary for IE >= 10*/

    mywindow.print();
    mywindow.close();
}