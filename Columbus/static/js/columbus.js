let is_company = document.getElementById('id_is_company');
let div_id_owner_company_registration_number = document.getElementById('div_id_owner_company_registration_number');
let div_id_owner_company_tax_nr = document.getElementById('div_id_owner_company_tax_nr');
let div_id_owner_company_contact_name = document.getElementById('div_id_owner_company_contact_name');
let div_id_owner_company_contact_phone = document.getElementById('div_id_owner_company_contact_phone');
let div_id_owner_company_contact_email = document.getElementById('div_id_owner_company_contact_email');

console.log(document.getElemetsByClass("company_div"));


if(is_company.checked) {
    //div_id_registration_number.style.display = "block";
    div_id_owner_company_registration_number.style.display = "block";
    div_id_owner_company_tax_nr.style.display = "block";
    div_id_owner_company_contact_name.style.display = "block";
    div_id_owner_company_contact_phone.style.display = "block";
    div_id_owner_company_contact_email.style.display = "block";
} else {
    //div_id_registration_number.style.display = "none";
    div_id_owner_company_registration_number.style.display = "none";
    div_id_owner_company_tax_nr.style.display = "none";
    div_id_owner_company_contact_name.style.display = "none";
    div_id_owner_company_contact_phone.style.display = "none";
    div_id_owner_company_contact_email.style.display = "none";
}
is_company.addEventListener('change', function() {
    if (this.checked) {
        //div_id_registration_number.style.display = "block";
        div_id_owner_company_registration_number.style.display = "block";
        div_id_owner_company_tax_nr.style.display = "block";
        div_id_owner_company_contact_name.style.display = "block";
        div_id_owner_company_contact_phone.style.display = "block";
        div_id_owner_company_contact_email.style.display = "block";
    } else {
        //div_id_registration_number.style.display = "none";
        div_id_owner_company_registration_number.style.display = "none";
        div_id_owner_company_tax_nr.style.display = "none";
        div_id_owner_company_contact_name.style.display = "none";
        div_id_owner_company_contact_phone.style.display = "none";
        div_id_owner_company_contact_email.style.display = "none";
    }
});