$(document).ready(function() {
    /// initAddressAutoComplete();
});

function initGeoCoder() {
    var geocoder = new google.maps.Geocoder({
    });
    document._geocoder = geocoder;
}

/*


    <div class="address-autocomplete-holder">
      <form><fieldset>
      <input type="text" class="address" id="address" 
      list="address-autocomplete-list" autocomplete="on" placeholder="Enter your address"/>
      <datalist id="address-autocomplete-list" class="autocompletes">
        <select>
        </select>
      </datalist>
      <button class="btn btn-m btn-g">Submit</button>
      </fieldset></form>
    </div>

*/

function initAddressAutoComplete() {
    initGeoCoder();

    $('.address').bind('keyup.autocomplete', function(e) {
        // allow alphanumeric characters, comma, and space
        if (((e.which < 48) && (e.which != 32)) 
            || ((e.which > 90) && (e.which != 188))) {
            return;
        }
        var $this = $(this);
        
        var val = $this.val();

        timeout = $this.data('autocomplete_timeout');

        if (! timeout) {
            timeout = setTimeout(function() {
                $this.data('autocomplete_timeout', null);
                //$('datalist').css('display','block');
                // API doesn't return anything for just numbers

                if (val.match(/[A-Za-z]/)) {
                    populateAutoComplete($this.val(), $this);
                }
            }, 600);
            $this.data('autocomplete_timeout', timeout);
        }
    })
}

function populateAutoComplete(str, $elem) {
    var latlng = new google.maps.LatLng(37.29576,-121.929865);
    var defaultBounds = new google.maps.LatLngBounds(
        new google.maps.LatLng(38, -123),
        new google.maps.LatLng(37, -121)
    );

    document._geocoder.geocode( {
        address: str,
        bounds: defaultBounds,
        region: 'US'
    }, function( results, status ) {
        if( status == google.maps.GeocoderStatus.OK ) {
            addresses = getAutoCompleteAddresses(results);
            
            var $autocomplete_area = $elem.parent().find('.autocompletes select');
            console.log(str, $elem, $autocomplete_area);
            $autocomplete_area.html(' ');

            addresses.forEach(function(address, i) {
                alert(address);
                $autocomplete_area.append('<option value="' + address + '">' + address + '</option>');
            });

            //$('.autocompletes').updatePolyfill();

        }
    });

}

function getAutoCompleteAddresses(results) {
    var addresses = [];

    results.forEach(function(result, i) {
        if (result['types'].indexOf('street_address') != -1) {
            addresses.push(results[i]['formatted_address']);
        }
    });
    return addresses;
        
}