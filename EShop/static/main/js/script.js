// "Корзина"
$(document).ready(function () {
  function totalQuantity() {
    // Відображення загальної кількості товару в корзині на сайті.
    var ProductInBasket = $('.products-in-basket');

    for (var i = 0, sum_quantity = 0, key, value; i < localStorage.length; i++) {
      key = localStorage.key(i);
      value = localStorage.getItem(key);
      sum_quantity = sum_quantity + +value
    }

    ProductInBasket.text(sum_quantity)
  }
  totalQuantity();
  
  // Форма добавлення товару в корзину.
  (function Cart() {
    var $quantityArrowMinus = $(".quantity-arrow-minus");
    var $quantityArrowPlus = $(".quantity-arrow-plus");
    var $quantityNum = $(".quantity-num");
    var $addCart = $('#addCart');
    var $itemPrice = $('#itemPrice');

    $quantityArrowMinus.click(quantityMinus);
    $quantityArrowPlus.click(quantityPlus);

    function addItem() {
      // Запис в Local Storage
      id = $addCart.attr('product_id');
      quantity = $('#quantity-num').val();
      if (quantity > 0) {
        localStorage.setItem(id, quantity);
        totalQuantity();
      }
    }
    function deleteItem() {
      id = $addCart.attr('product_id');
      quantity = $('#quantity-num').val();
      localStorage.removeItem(id);
      totalQuantity();
    }
    function quantityMinus() {
      if ($quantityNum.val() > 1) {
        $quantityNum.val(+$quantityNum.val() - 1);
        addItem();
      }
      else if ($quantityNum.val() == 1){
        $quantityNum.val(+$quantityNum.val() - 1);
        deleteItem();
      }
    }
    function quantityPlus() {
      $quantityNum.val(+$quantityNum.val() + 1);
      addItem();
    }
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