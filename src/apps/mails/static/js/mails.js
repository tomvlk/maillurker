$(function () {
  'use strict';

  /**
   * Checkboxes.
   */
  $('.table-check-all').click(function () {
    var state = $(this).is(':checked');

    $('.table-body-checkbox').each(function () {
      $(this).prop('checked', state);
    });
  });


  /**
   * Details View.
   */
  $('.table-body-detail-action').click(function () {
    var template = $('#message-modal-template').html();
    var listLinkTemplate = $('#message-modal-list-link-template').html();

    var messageId = $(this).parents('tr').data('messageId');
    var dialog = bootbox.dialog({
      title: 'Message details',
      size: 'large',
      message: '<div class="text-center"><h6><i class="fa fa-spin fa-spinner"></i> Loading...</h6></div>'
    });
    dialog.init(function() {
      var body = $(dialog).find('.bootbox-body');

      var message;
      var parts;
      var part;

      // Function called when all actions are completed.
      function done () {
        body.html(template);
        $(dialog).find('.modal-title').text('Message from \'' + message.sender_name + '\'');
        $(dialog).find('.modal-title').append('&nbsp;&nbsp;&nbsp;' +
          '<a href="/mails/download/'+message.id+'" class="btn btn-default btn-sm" target="_blank">' +
          '<i class="fa fa-download"></i> Download .eml' +
          '</a>'
        );

        // Format generic fields.
        Object.keys(message).forEach(function (key) {
          var elements = body.find('.field.'+key);
          if (elements.length > 0) {
            elements.text(message[key]);
          }
        });

        // Custom formats
        var addressFormatter = function (entry) {
          return '' + entry[0] + ' <' + entry[1] + '>, ';
        };
        var headersText = '';
        for (var headerKey in message.headers) {
          if (message.headers.hasOwnProperty(headerKey))
            headersText += headerKey + ': ' + message.headers[headerKey] + '\n';
        }
        body.find('.field.recipients_to_custom').text(message.recipients_to.map(addressFormatter));
        body.find('.field.recipients_cc_custom').text(message.recipients_cc.map(addressFormatter));
        body.find('.field.recipients_bcc_custom').text(message.recipients_bcc.map(addressFormatter));
        body.find('.field.headers_custom').text(headersText);

        // Links to parts and attachments
        var partsList = body.find('div.parts');
        var attachmentsList = body.find('div.attachments');

        for (var idx in message.parts) {
          if (! message.parts.hasOwnProperty(idx)) continue;
          var part = message.parts[idx];
          var listLink = $($.parseHTML('' + listLinkTemplate));

          if (part.is_attachment) {
            listLink.find('.icon').addClass('fa fa-paperclip');
            listLink.find('.name').text('Attachment #'+idx+', '+part.type+' (download)');
            listLink.attr('href', '/mails/' + message.id + '/parts/' + part.id + '/download');
            attachmentsList.append(listLink);
          } else {
            listLink.find('.icon').addClass('fa fa-envelope-o');
            listLink.find('.name').text('Part #'+idx+', '+part.type+'');
            listLink.attr('href', '/mails/' + message.id + '/parts/' + part.id);
            partsList.append(listLink);
          }
        }

        return {then: function() {}}
      }

      // Get message and first part.
      $.get('/api/mails/' + messageId + '/').then(function (data) {
        message = data;
        parts = data.parts;

        if (! parts) return done();
        return $.get('/api/parts/' + parts[0].id + '/');
      }).then(function (data) {
        part = data;
        return done();
      });
    });
  });

});
