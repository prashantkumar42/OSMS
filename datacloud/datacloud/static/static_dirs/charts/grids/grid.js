      var gridster;

      $(function() {

        gridster = $(".gridster ul").gridster({
          widget_base_dimensions: [100, 100],
          widget_margins: [5, 5],
          helper: 'clone',
          resize: {
            enabled: false,
            max_size: [4, 4],
            min_size: [1, 1]
          }
        }).data('gridster');


      });

