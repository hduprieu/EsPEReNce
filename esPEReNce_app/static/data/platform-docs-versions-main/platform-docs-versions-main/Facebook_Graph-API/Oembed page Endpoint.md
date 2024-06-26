# Resource URL: https://developers.facebook.com/docs/graph-api/reference/oembed-page/
Oembed Page
===========

Reading
-------

OembedPage

### Example

HTTPPHP SDKJavaScript SDKAndroid SDKiOS SDK[Graph API Explorer](https://developers.facebook.com/tools/explorer/?method=GET&path=oembed_page&version=v19.0)

    GET /v19.0/oembed_page HTTP/1.1
    Host: graph.facebook.com

    /* PHP SDK v5.0.0 */
    /* make the API call */
    try {
      // Returns a `Facebook\FacebookResponse` object
      $response = $fb->get(
        '/oembed_page',
        '{access-token}'
      );
    } catch(Facebook\Exceptions\FacebookResponseException $e) {
      echo 'Graph returned an error: ' . $e->getMessage();
      exit;
    } catch(Facebook\Exceptions\FacebookSDKException $e) {
      echo 'Facebook SDK returned an error: ' . $e->getMessage();
      exit;
    }
    $graphNode = $response->getGraphNode();
    /* handle the result */

    /* make the API call */
    FB.api(
        "/oembed_page",
        function (response) {
          if (response && !response.error) {
            /* handle the result */
          }
        }
    );

    /* make the API call */
    new GraphRequest(
        AccessToken.getCurrentAccessToken(),
        "/oembed_page",
        null,
        HttpMethod.GET,
        new GraphRequest.Callback() {
            public void onCompleted(GraphResponse response) {
                /* handle the result */
            }
        }
    ).executeAsync();

    /* make the API call */
    FBSDKGraphRequest *request = [[FBSDKGraphRequest alloc]
                                   initWithGraphPath:@"/oembed_page"
                                          parameters:params
                                          HTTPMethod:@"GET"];
    [request startWithCompletionHandler:^(FBSDKGraphRequestConnection *connection,
                                          id result,
                                          NSError *error) {
        // Handle the result
    }];

If you want to learn how to use the Graph API, read our [Using Graph API guide](https://developers.facebook.com/docs/graph-api/using-graph-api/).

### Parameters

| Parameter | Description |
| --- | --- |
| `adapt_container_width`<br><br>boolean | Default value: `true`<br><br>Try to fit inside the container width. |
| `hide_cover`<br><br>boolean | Default value: `false`<br><br>Hide cover photo in the header. |
| `maxheight`<br><br>int64 | Maximum height of returned media. |
| `maxwidth`<br><br>int64 | Maximum width of returned media. |
| `omitscript`<br><br>boolean | Default value: `false`<br><br>If set to true, the returned embed HTML code will not include any javascript. |
| `sdklocale`<br><br>string | sdklocale |
| `show_facepile`<br><br>boolean | Default value: `true`<br><br>Show profile photos when friends like this. |
| `show_posts`<br><br>boolean | Default value: `true`<br><br>show\_posts |
| `small_header`<br><br>boolean | Default value: `false`<br><br>Use the small header instead. |
| `url`<br><br>URI | The page's url.<br><br>Required |

### Fields

| Field | Description |
| --- | --- |
| `height`<br><br>int32 | The height in pixels required to display the HTML.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `html`<br><br>string | The HTML used to display the page.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `provider_name`<br><br>string | Name of the provider (Facebook)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `provider_url`<br><br>string | URL of the provider (Facebook)<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `type`<br><br>string | The oEmbed resource type. See https://oembed.com/.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `version`<br><br>string | Always 1.0. See https://oembed.com/<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |
| `width`<br><br>int32 | The width in pixels required to display the HTML.<br><br>[Default](https://developers.facebook.com/docs/graph-api/using-graph-api/#fields) |

### Error Codes

| Error | Description |
| --- | --- |
| 100 | Invalid parameter |
| 200 | Permissions error |

Creating
--------

You can't perform this operation on this endpoint.

Updating
--------

You can't perform this operation on this endpoint.

Deleting
--------

You can't perform this operation on this endpoint.

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)