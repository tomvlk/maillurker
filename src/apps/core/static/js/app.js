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
    $('.action-selection-count').text('' + number);
    $('.action-buttons button[data-enabled="1"]').prop('disabled', number === 0);
  });

  $('.action-buttons button').click(function () {
    var action = $(this).data('action');
    var number = $('.table-body-checkbox:checked').length;
    var items = [];

    $('.table-body-checkbox:checked').each(function() {
      try {
        items.push(parseInt($(this).val()));
      } catch (error) {
        // ignore
      }
    });

    if (! number || ! items) return;

    function execute (callback) {
      if (action == 'download') {
        return window.location = '/mails/download/' + (items.join(','));
      }

      $.ajax({
        url: '/api/mails/' + action + '/',
        data: JSON.stringify({items: items}),
        dataType: 'json',
        contentType: 'application/json; charset=utf-8',
        method: 'POST',
      }).done(function (data) {
        console.log(data);
        return callback(null);
      }).fail(function (jqXHR, textStatus, errorThrown) {
        return callback(errorThrown);
      });
    }

    // Ask for confirm
    if (action == 'remove' || action == 'download' || action == 'forward') {
      bootbox.confirm({
        title: 'Are your sure?',
        message: 'Are you sure you want to ' + action + ' ' + number + ' of items?',
        buttons: {
          cancel: {
            label: '<i class="fa fa-times"></i> Cancel'
          },
          confirm: {
            label: '<i class="fa fa-check"></i> Confirm'
          }
        },
        callback: function (result) {
          if (result) {
            execute(function(err) {
              if (! err && action !== 'download') return window.location.reload();
              console.error(err);
            });
          }
        }
      });
    }
  });
});
