$('main .markup-chevron').removeClass('icon-chevron-up').addClass('icon-chevron-down');
 $('main .markup-toggle').click(function() {
     $(this).parent().next().toggleClass('hide');
     $(this).next().toggleClass('hide').removeClass('text-blue').text('Copy'); // Toggle the clipboard copy. Should only display when code is viewable
     $(this).toggleClass('toggled');

     if ($(this).hasClass('toggled')) {
         $(this).find('.markup-chevron').removeClass('icon-chevron-down').addClass('icon-chevron-up');
         $(this).find('.markup-label').text('Hide Details ');
     }
     else if (!$(this).hasClass('toggled')) {
         $(this).find('.markup-chevron').removeClass('icon-chevron-up').addClass('icon-chevron-down');
         $(this).find('.markup-label').text('View Details ');
     }
 });
