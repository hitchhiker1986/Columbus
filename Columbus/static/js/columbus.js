let is_company = document.getElementById('id_is_company');
let div_id_registration_number = document.getElementById('div_id_registration_number');

if(is_company.checked) {
    div_id_registration_number.style.display = "block";
} else {
    div_id_registration_number.style.display = "none";
}
is_company.addEventListener('change', function() {
    if (this.checked) {
        div_id_registration_number.style.display = "block";
    } else {
        div_id_registration_number.style.display = "none";
    }
});