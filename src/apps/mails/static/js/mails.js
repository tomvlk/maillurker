$(function () {
  'use strict';

  /**
   * Checkboxes.
   */
  $('.table-check-all').click(function () {
    var state = $(this).is(':checked');

    $('.table-body-checkbox').each(function() {
      $(this).prop('checked', state);
    });
  });

  alert(1);

});
