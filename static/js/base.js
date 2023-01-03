
let cart_up_button = document.getElementsByClassName("upd-cart");
let cart_rm_button = document.getElementsByClassName("rmv-cart");
let cart_label = document.getElementById('cart_up_num')
let num=1
for (let i = 0; i < cart_up_button.length; i++){
    cart_up_button[i].addEventListener('click', function () {
        let pro_id = this.dataset.product
        let action = this.dataset.action
        cart_label.innerHTML = num
        num++
       
    })
}



