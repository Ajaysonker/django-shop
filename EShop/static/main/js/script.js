// "Корзина"
$(function () {
  // localStorage.clear();
  function totalQuantity() {
    // Відображення загальної кількості товару в корзині на сайті.
    let $ProductInBasket = $('.products-in-basket');
    let sum_quantity = 0;
    let key, value;

    for (let i = 0; i < localStorage.length; i++) {
      key = localStorage.key(i);
      value = localStorage.getItem(key);
      product_data = JSON.parse(value);
      sum_quantity = sum_quantity + +product_data.quantity;
    }

    $ProductInBasket.text(sum_quantity);
  }
  totalQuantity();

  (function modalCart() {
    // Форма добавлення товару в корзину.

    $('.btn-cart').click(function modalDataRender() {
      // Заповнення модальної форми, добавлення товару в корзину.
      let str_product_data = $(this).attr('product_data');
      let product_data = JSON.parse(str_product_data);

      $('.modal_product_img').attr('src', product_data.image);
      $('.modal-product-name').text(product_data.name);
      $('.modal_product_price').text(product_data.price + " " + '₴');
      $('#addCart').attr('modal_product_id', product_data.id);
      $('#addCart').attr('modal_product_data', str_product_data);

      if (localStorage.getItem(product_data.id) !== null) {
        let value = localStorage.getItem(product_data.id);
        product_data = JSON.parse(value);
        $quantityNum.val(product_data.quantity);
      } else {
        $quantityNum.val(1);
        addItem();
      }

      price = +product_data.price;
      quantity = +$quantityNum.val();
      modalTotalPrice();

      // декор
      if ($quantityNum.val() < 2) {
        $('.svg-subtract').hide();
        $('.svg-delete').show();
      }
    })

    let $quantityNum = $(".quantity-num");

    function modalTotalPrice() {
      let price = $('.modal_product_price').text().replace('₴', '');
      let quantity = $quantityNum.val();
      let total_price = (price * quantity).toFixed(2);
      $('#total_price').text(total_price + " " + '₴');
    }

    function addItem() {
      // Додати товар в корзину.
      let id = $('#addCart').attr('modal_product_id');

      let product_data = JSON.parse($('#addCart').attr('modal_product_data'));
      let quantity = $quantityNum.val();
      let new_product_data = $.extend(product_data, { 'quantity': quantity });

      if (quantity > 0) {
        localStorage.setItem(id, JSON.stringify(new_product_data));
        totalQuantity();
      }
    }

    function deleteItem() {
      // Видалити товар з корзини.
      let id = $('#addCart').attr('modal_product_id');
      localStorage.removeItem(id);
      totalQuantity();
    }

    $(".quantity-arrow-plus").click(function quantityPlus() {
      //Збільшити кількість товару на 1.
      $quantityNum.val(+$quantityNum.val() + 1);
      addItem();
      modalTotalPrice();

      // декор
      if ($quantityNum.val() > 1) {
        $('.svg-subtract').show()
        $('.svg-delete').hide()
      }
    })

    $(".quantity-arrow-minus").click(function quantityMinus() {
      //Зменшити кількість товару на 1 або видалити якщо кількість рівна нулю.
      if ($quantityNum.val() > 1) {
        $quantityNum.val(+$quantityNum.val() - 1);
        addItem();
      } else if ($quantityNum.val() == 1) {
        $quantityNum.val(+$quantityNum.val() - 1);
        deleteItem();
        $('#productDetailModal').modal('hide')
      }

      modalTotalPrice();

      // декор
      if ($quantityNum.val() < 2) {
        $('.svg-subtract').hide()
        $('.svg-delete').show()
      }
    })
  })();


  // order_checkout cart

  (function renderCheckoutCart() {
    let $CheckoutCart = $('.checkout-cart > .card-body');
    let $totalPrice = $('.total-price');
    let total_price = 0;

    for (let i = 0; i < localStorage.length; i++) {
      let key = localStorage.key(i);
      let value = localStorage.getItem(key);
      let product_data = JSON.parse(value);
      $CheckoutCart.append(
      '<div class="row align-items-center cart-item">' +
        '<div class="col h6">' + product_data.name + '</div>' + 
        '<div class="col-2 px-0"><img src="'+ product_data.image +'" class="card-img" alt=""></div>' +
        '<div class="col-3">' + product_data.price + '₴</div>' +
        '<div class="col-1 px-0">' + product_data.quantity + '</div>' +
      '</div>'
      );
      total_price = total_price + (product_data.price * product_data.quantity);
    }

    $totalPrice.text('Загальна вартість: ' + total_price.toFixed(2) + '₴');
  })();
});


// Випадаюче меню "Категорії"
$(document).on('click', '.dropdown-menu', function (e) {
  e.stopPropagation();
});

// clickable on mobile view
if ($(window).width() < 992) {
  $('.has-submenu a').click(function (e) {
    e.preventDefault();
    $(this).next('.megasubmenu').toggle();

    $('.dropdown').on('hide.bs.dropdown', function () {
      $(this).find('.megasubmenu').hide();
    })
  });
}