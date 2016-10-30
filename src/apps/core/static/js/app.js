$(function () {
  'use strict';
  /****************************
   * Mail + Sidebar filtering *
   ****************************/

  /**
   * Sidebar - Action
   */
  $('.table-body-checkbox, .table-check-all').change(function() {
    var number = $('.table-body-checkbox:checked').length;
    $('#action-selection-count').text('' + number);

    var disabled = true;
    if (number > 0) {
      disabled = false;
    }
    $('#action-buttons button').prop('disabled', disabled);
  });

});
