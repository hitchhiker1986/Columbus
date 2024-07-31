let is_company = document.getElementById('id_is_company');
let company_div = document.getElementById("company_div");
//let div_id_registration_number = document.getElementById('div_id_registration_number');
console.log(company_div)
if(is_company.checked) {
    //div_id_registration_number.style.display = "block";
    company_div.style.display = "block";
} else {
    //div_id_registration_number.style.display = "none";
    company_div.style.display = "none";
}
is_company.addEventListener('change', function() {
    if (this.checked) {
        //div_id_registration_number.style.display = "block";
        company_div.style.display = "block";
    } else {
        //div_id_registration_number.style.display = "none";
        company_div.style.display = "none";
    }
});

