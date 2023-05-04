function getCookie(name) {
    let matches = document.cookie.match(new RegExp(
        "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
    ));
    return matches ? decodeURIComponent(matches[1]) : undefined;
}

async function trainForm(event) {
    event.preventDefault();
    let formData = new FormData(event.target);
    let response = await fetch(`${window.location.origin}/api/v1/trained-model/check/`, {
            method: 'POST',
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                seniority: formData.get("seniority"),
                home: formData.get("home"),
                time: formData.get("time"),
                age: formData.get("age"),
                marital: formData.get("marital"),
                records: formData.get("records"),
                job: formData.get("job"),
                expenses: Number(formData.get("expenses1")) + Number(formData.get("expenses2")) + Number(formData.get("expenses3")) + Number(formData.get("expenses4")),
                income: formData.get("income"),
                assets: formData.get("assets"),
                debt: formData.get("debt"),
                amount: formData.get("amount"),
                price: formData.get("price"),
                finrat: formData.get("finrat"),
                savings: formData.get("savings"),
                pasport: formData.get("pasport"),
                snils: formData.get("snils"),
                inn: formData.get("inn"),
            })
        }
    );

    let result = await response.json();
    console.log(result);
}