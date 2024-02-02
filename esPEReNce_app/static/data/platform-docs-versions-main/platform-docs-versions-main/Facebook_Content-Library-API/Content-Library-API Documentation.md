# Resource URL: https://developers.facebook.com/docs/content-library-api/overview
Overview
========

Meta Content Library API provides access to real-time data from public discussions on Facebook and Instagram, equipping researchers to study existing topics of interest as well as understand evolving or emerging topics on our platforms.

Content Library API can be accessed either through Meta's Researcher Platform or through an approved third-party cleanroom environment. The following third-party cleanroom environments are approved as of Content Library API version 2.0:

* Inter-university Consortium for Political and Social Research (ICPSR) at the University of Michigan

User documentation for third-party cleanroom interfaces is outside the scope of the Meta Content Library API documentation and can instead be provided by the third-party's system administrator.

Content Library API client
--------------------------

When you access the API through Meta's Researcher Platform, you use our Content Library API Client which runs on Jupyter and with which you can create Jupyter notebooks. Once you have created a notebook, you can import our Python3 or R Content Library API client module which allows you to perform queries using the API. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start).

The Content Library API Client allows you to access a variety of fields on the following data. Information and content from public entities listed below will be returned; however, certain data that could potentially identify users (such as tags in Facebook) will be redacted or omitted in API responses.

* Facebook Pages
* Facebook groups
* Facebook events
* Facebook posts
* Instagram business and creator accounts, and a subset of personal accounts that match qualification criteria
* Instagram posts

Note that public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT3dyyMutGT_rdMejwa0iOefCSmGb7VnqRWLUt5lUWA04PiJSrO6i80IcC_-XQncNKD5slXJFEOCsp1MJHMEtFOECE-mhsKd8WIuRcGRs-uTbsV75-Jq-eig6sr2U2brFxyxLfIexBChdqMI) and have either a verified badge or 50,000 or more followers. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT1blgqtfrQ0FTPYYkSwV2zuDc3Ao8wLA4sb0SuqcOsjgn1wYQRkPkUFsWEonpVjJHU0puO3b8irHbGqgzTPTnuiP4iYW3K7MTF4JyE9CL1Mt_5WS1Mjm56moCEBiYqEhNoPDycFlE71Fv11) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription.

VPN
---

You access the API through our virtual private network (VPN) using OpenVPN. Follow the OpenVPN Setup instructions in [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn how to install and configure the OpenVPN client.

Data dictionary
---------------

We provide a detailed [Data dictionary](https://developers.facebook.com/docs/content-library-api/data) that describes the data names displayed in the Meta Content Library (the Name column) if applicable, and the corresponding API fields returned in Content Library API search responses (the API field column).

Meta Content Library
--------------------

[Meta Content Library](https://www.facebook.com/transparency-tools/content-library/dataset/1119037145491882/about/) is a web-based tool that allows researchers to explore and understand data across Facebook and Instagram by offering a comprehensive, visual, searchable collection of publicly accessible content—the same content that is also accessible through the Content Library API. The web-based user interface allows you to explore data, test out search parameters, and assess whether the resulting data is appropriate for your planned research. No knowledge of query or programming languages is needed.

Code examples
-------------

Code examples in this documentation use a tabbed code block with tabs for R and Python. Click the tab for the language of your choice to display the appropriate code. This is an example:

RPython

    Click the R tab to display R code here

    Click the Python tab to display Python code here

You can copy the code in either tab and paste it into a Jupyter notebook cell for the same language (R or Python).

Learn more
----------

* [Frequently asked questions](https://developers.facebook.com/docs/content-library-api/disclosures)
    
* [Search quality approach](https://developers.facebook.com/docs/content-library-api/search-quality)
    
* [Researcher Platform](https://developers.facebook.com/docs/researcher-platform)
    
* [Meta Content Library](https://www.facebook.com/transparency-tools/content-library/dataset/1119037145491882/about/)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/get-access
Get access
==========

Meta is partnering with the Inter-university Consortium for Political and Social Research (ICPSR) at the University of Michigan to vet applications and assist in onboarding to Meta Content Library and API.

Eligibility requirements
------------------------

To be eligible for product access, researchers must be affiliated with a qualified academic institution or a qualified research institution. Researchers from different disciplinary and professional backgrounds are welcome to apply.

For academic institutions, _qualified_ means the institution meets all of the following criteria. It is:

* Dedicated to the pursuit of education and research.
    
* Accredited, as indicated by recognized standards and evidence on the institution's website (such as a university), or as demonstrated by documentation provided to ICPSR.
    
* Qualified to grant academic degrees (such as undergraduate, graduate, doctoral).
    
* A not-for-profit endeavor (in other words, not a business whose sole purpose is to make a profit).
    

For research institutions, _qualified_ means the institution is a non-university organization, institute, or society/entity which operates as a not-for-profit entity and holds scientific or public interest research as a primary purpose or core activity.

Application and access process
------------------------------

### **Step 1: Review application requirements and submit an application.**

To help ensure a fair and independent application and evaluation process, Meta has partnered with the Inter-university Consortium for Political and Social Research (ICPSR) based at the University of Michigan, to assess researcher qualifications and review submissions from global applicants. You can find an overview of the application process and data tools on ICPSR’s [Social Media Archive (SOMAR)](https://l.facebook.com/l.php?u=https%3A%2F%2Fsocialmediaarchive.org%2Frecord%2F52&h=AT1_7jhF518K63MvwoIYHoRQy48nUhAJ2xKqdwirZdhZro1rwJu5azJwnTitznBZq2WZO5Y5u9jDJQ7lrymwDAho219EjgHwZKLOsvWu6eBv4yegO9wSkrGfMwj1smk6L4Cm6x4j5eU6AOVY). We also encourage you to familiarize yourself with the Meta Content Library [application page](https://l.facebook.com/l.php?u=https%3A%2F%2Fsomar.infoready4.com%2F%23freeformCompetitionDetail%2F1910793&h=AT3mimCW7chqKjud0Ei_dDSATmOQJg1gDAT6_z5LL-lX9wWhKUKRJPZySy15pg0ihqbXAqWs53OWzaKVIcA6KeUYi-PsWX_-q9PJDkaVktFFiU8STZFnQ1dhh-M8q6iQuSfcEU2qLIhxTMnL) on the SOMAR site and [ICPSR’s application guide](https://l.facebook.com/l.php?u=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F1iN4KOvFaYGZro23cB4j1FveouXMBcZnKl-yTUyx6fCg%2Fedit%3Fusp%3Dsharing&h=AT2sKmxh8ehYHpKRYcSLgUNTg1A2BBRMOrPqRFmPPMtfrEXKCz__bRnxRr-2B75PRRdE71snnEUUPSF6QJ0aRfxeee2_bTNAPgKO_3HLtSqVVp7roB6-09VsmTF-nQUtXRv7HFXGO1lYU0Y2) before applying.

ICPSR will notify Meta and the applicant if the application is approved. Researchers can expect the review process to take between four and six weeks.

### **Step 2: Fulfill additional data access requirements.**

The Meta Content Library API is available for researchers to access on ICPSR’s Virtual Data Enclave. A Data Use Agreement between ICPSR and your institution must be executed before you are granted access to the platform. More information about ICPSR’s requirements can be found in [ICPSR’s application guide](https://l.facebook.com/l.php?u=https%3A%2F%2Fdocs.google.com%2Fdocument%2Fd%2F1iN4KOvFaYGZro23cB4j1FveouXMBcZnKl-yTUyx6fCg%2Fedit%3Fusp%3Dsharing&h=AT2BrWHEFA13x0VKdcfzn2TLbZ1KFS_uI7U988YxliWGwxhQ99FW71E0CZwOY9lTjJRBHu9pnDx0wxvT1VPZyixyWl7KZQ4kQeWVQNty3Sg4MsuIhhGMPB4Qx_MR432iroeoKWR5LqVo5dAE).

Meta will follow up with approved researchers with information on how to access and onboard to the Meta Content Library user interface (UI). The UI can be used separately or in conjunction with the Content Library API.

### **Step 3: Gain access.**

Access to Meta Content Library and Content Library API will be provisioned once all access requirements are fulfilled. In order to continue accessing the tools, you will need to recertify your affiliation with your institution and research project on an annual basis.

Frequently asked questions about access, eligibility, and publication
---------------------------------------------------------------------

#### Are global researchers eligible for access to Content Library and API?

We welcome global researchers, but access to or use of our tools and data must comply with all applicable laws, rules and regulations. In addition, the researcher applicant, and any academic university or institution with which the applicant is affiliated, must not be in a jurisdiction that is the target of sanctions imposed by the United States, United Kingdom, European Union or United Nations.

#### Do researchers have to pay to access Content Library and API?

No. There are no fees associated with access or computation.

#### Do researchers have to reapply for access if they change their research topic or proposal?

If the researcher has made any substantive changes to their research topic, proposal or research ethics documentation since having their application approved by the Inter-university Consortium for Political and Social Research (ICPSR), they must reapply for access.

#### Do global researchers affiliated with institutions not in the United States still need to apply through ICPSR?

Yes. All Content Library and API researcher applications are processed and reviewed by ICPSR.

#### How does the application and access process work for researchers who collaborate together or as part of a larger research team?

ICPSR will process and review applications from teams of researchers with a clearly identified research lead and collaborators. For more information please reference the ICPSR [application page.](https://l.facebook.com/l.php?u=https%3A%2F%2Fsomar.infoready4.com%2F%23freeformCompetitionDetail%2F1910793&h=AT0zCIa7wEHdY3xzVHqe519iM3KrQO1yMBASsu-Yne2ptRyUJUqGcBs41HJjyJYjf9IALNFxTS6Qj1EqjPr-Kk_i1_ep_Mbqz-wjZaGAYFuUXzz0HOnkVPj3fWmHbm75eA5HLZeiY_kedlDY)

#### Does Meta place any restrictions on how I can publish with data from the Meta Content Library and API?

Researchers may publish Research Outputs (such as tables, graphs, and analysis), but may not publish any Confidential Information or Personal Data. For publications based solely on Content Library and/or API, Meta will not ask to review research manuscripts prior to publication. However, we ask that researchers follow Meta’s attribution guidelines (see [Citations](https://developers.facebook.com/docs/content-library-api/citations)) and provide notice upon publishing.

Please refer to the [Product Terms for Meta Research Tools](https://l.facebook.com/l.php?u=https%3A%2F%2Ftransparency.fb.com%2Fresearchtools%2Fproduct-terms-meta-research&h=AT32BdF80pQD6DJkGa3ypSE9sksL7mnepiZrSdxEHMlqoy96YZfaf4_1Fk2xXqyH8BvatYw4vwp0gtR6qNUDLYkLlKVhK_susZxqiLrHeUQK11JmhklP06P6zSEn9Yf9XGOOeUG3dCSzKvoH) for the requirements and conditions related to publication.

Learn more
----------

* [Inter-university Consortium for Political and Social Research (ICPSR)](https://l.facebook.com/l.php?u=https%3A%2F%2Fwww.icpsr.umich.edu%2Fweb%2Fpages%2Fabout%2F&h=AT3Ct6QtFLXo0rcth7PygRVH-MbyPZ_cJfDNGCiCxkSVybXH1GusxnM-lUfKOduXx6lKGG2Rv55Uy0MUS_Eq6pUxIrW7Ga2RjAmGEi1ywVIJEw80b0zIjM7h0jamur3TxbZBvgQqSTfWfUaJ)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/changelog
Meta Content Library API changelog
==================================

The changelog lists product and documentation changes per release, in reverse chronological order.

Version 2.0, January 30 2024
----------------------------

Meta Content Library API v2.0 has been enhanced with the following new features:

* You can now search Facebook and Instagram posts by post ID. Use the `post_ids` parameter, specifying one or more post IDs that you obtained from a previous search. See [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts) and [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts).
    
* A subset of Instagram personal accounts that match qualification criteria can now be included in results when you search for Instagram account information or for posts from Instagram accounts. Public Instagram accounts include professional accounts for businesses and creators. They now also include a subset of personal accounts that have account privacy set to public and have either a verified badge or 50,000 or more followers. A verified badge in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. See [Guide to Instagram accounts data](https://developers.facebook.com/docs/content-library-api/guide-ig-accounts) and [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts).
    
* You can now filter posts from Facebook Pages by the page admin’s location country. Set the new `admin_countries` parameter to include one or more country codes of your choice. See [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts).
    
* Multimedia (photos and videos) can now be included in search post results for both Instagram and Facebook. This feature is only available if you are accessing the API in an approved third party cleanroom environment, and only if that environment supports retrieval of multimedia. The feature is not available in Researcher Platform. See [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts) and [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts).
    
* The citation format was updated with a new Digital Object Identifier (DOI) that specifies version 2.0. Older release DOIs are still available for reference. See [Citations](https://developers.facebook.com/docs/content-library-api/citations).
    

Version v1.0 update, December 15 2023
-------------------------------------

The following changes were implemented:

* Search quality metrics were updated/improved. See [Search quality approach](https://developers.facebook.com/docs/content-library-api/search-quality).
    
* Due to the improved search quality, the "beta" designation on version 1.0 was removed.
    
* The citation format was updated with a new Digital Object Identifier (DOI) that does not include a beta designation. See [Citations](https://developers.facebook.com/docs/content-library-api/citations).
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/quick-start
Getting started
===============

You can work with Meta Content Library API within Meta's Researcher Platform or within an approved third-party cleanroom environment. The getting started procedure documented here is specific to Researcher Platform which runs a modified version of Jupyter and provides you with a virtual data cleanroom where you can securely search for and analyze data. If you are accessing the Content Library API through a third-party cleanroom environment, you will be provided with getting started instructions from the cleanroom's system administrator.

To get up and running with Content Library API in Researcher Platform:

* [Set up OpenVPN](#vpn-cl-api)
    
* [Log in to the Researcher Platform URL](#log-in-api)
    
* [Create a Jupyter notebook](#notebook-cl-api)
    
* [Import the Content Library API client](#client-library)
    
* [Test with a basic search](#test-basic-example)
    

Set up OpenVPN
--------------

Content Library API can only be accessed through a Virtual Private Network (VPN). This section shows you how to install and configure the OpenVPN client and connect to our VPN server. Once connected, you will be able to access Meta Content Library API.

#### Step 1: [Download and install OpenVPN](https://l.facebook.com/l.php?u=https%3A%2F%2Fopenvpn.net%2Fclient%2F%3Ffbclid%3DIwAR0Y0YhJ92gWqV68O7jjQXo-tv9aCO094M5q3ttl1wEwa9nDHLkOOlopi60&h=AT0Wkd4R7eRmdqBMaeplJfE9Ys1Nvlb51wigV_gOV8QeZttKWgyRKQT6jUJTIVrCjHl7Q8r7nB5gfvJPZntlZYbDfB9BQYDH8tyLLopu0eYTPiO7Nh5VV-2-3LAV2uQ4yEvEd5ULeeRhZDXN)

When the setup wizard completes, OpenVPN Connect launches and you will be required to accept the OpenVPN Inc. Data Collection, Use and Retention policy to continue.

#### Step 2: Set up your profile

In the Import Profile window, select the **UPLOAD FILE** tab.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/359841127_304985435250473_5304206694181437663_n.png?_nc_cat=107&ccb=1-7&_nc_sid=f537c7&_nc_ohc=HVyfCGNKtuUAX_Ha_4J&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCUlvtJLVqqitcH1hS472T0xZCK1AaUwjGcyhT0hv5tnw&oe=65BF53A2)  
  

#### Step 3: [Download the OpenVPN configuration file](https://facebook.com/transparency-tools/vpn-credentials)

Clicking this link downloads the OpenVPN configuration file (fortVpnCredentials.ovpn) to your computer (check your downloads folder). Once downloaded, drag and drop the file into the Import Profile window.

#### Step 4: Connect to the VPN

In the Imported Profile window, click **CONNECT**.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/361947748_335117498837885_4826508458856907283_n.png?_nc_cat=107&ccb=1-7&_nc_sid=f537c7&_nc_ohc=bpa2hUI-G3IAX84bKLo&_nc_ht=scontent-cdg4-2.xx&oh=00_AfCGnvFOkljCRE5sHQwWGfBXu4PGBBgQykuGrCeYvl_7aA&oe=65BF0A8A)  
  

Once successfully connected, you will see this window:

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/361921794_727264049161457_5975480060212799981_n.png?_nc_cat=105&ccb=1-7&_nc_sid=f537c7&_nc_ohc=2dP9ltApeesAX-aCjq_&_nc_ht=scontent-cdg4-1.xx&oh=00_AfDUuCZk_Uc-dLJwdR40Sp8UVdwFWMs5DvGwZVdAd3sIfw&oe=65BE774E)

While you are connected to our VPN server, all of your internet traffic is routed through it, so be sure to disconnect when you are finished.

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/359843298_233572166287463_6401952988758247237_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=uKZH-1uJiS8AX8N_wyr&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCoLc717BjZv3SidQtl22_RIchzIKPqbWkjpNz0ppHG7g&oe=65BED4E4)

Log in to the Researcher Platform URL
-------------------------------------

While connected to the VPN, go to the [Researcher Platform URL](https://l.facebook.com/l.php?u=https%3A%2F%2Fcontent-library-api.fb-researchtool.com%2F&h=AT2Y8XmPJZzm5Nc9u15cmbPiXZZXtnmDbbfLgDRVPmKIhAA9QqSdsGRrdVlqw7LwrMeYYp-VUjbI2Rah-wCbRfZnjelNaSnsamwCaYMIdN3Iq1jqSG1TU1qUkpjMXk8xoLIOkxkvOnnjvjoP).

Log in to the site using your Facebook credentials. This will spin up an instance of JupyterHub server for your use in the Researcher Platform.

You will be offered the choice of CPU or GPU server. You can learn more about the difference between the two [here](https://developers.facebook.com/docs/researcher-platform/features/GPU) and there is complete documentation on [Researcher Platform here](https://developers.facebook.com/docs/researcher-platform).

Create a Jupyter notebook
-------------------------

To create a new notebook:

1. In your Jupyter hub environment, click the blue "+" symbol in the upper left corner of the window.
    
2. Under **Notebook** in the Launcher tab, select **Python 3** or **R** according to your preferred language. This creates and opens a new Jupyter notebook.
    

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/361395333_529381645981378_6324697782074898886_n.png?_nc_cat=108&ccb=1-7&_nc_sid=f537c7&_nc_ohc=yDI4S7jmn3QAX-frxLf&_nc_ht=scontent-cdg4-1.xx&oh=00_AfD_xBmkdFz4rOQhblccjzFG1M06RvWivvY0PV8JzW927A&oe=65BE4391)

To name the notebook, right-click the notebook in the left navigation bar and select **Rename**.

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/362621684_301900822211537_8967768774365526112_n.png?_nc_cat=104&ccb=1-7&_nc_sid=f537c7&_nc_ohc=WrCzH_P36HYAX90hjz8&_nc_ht=scontent-cdg4-3.xx&oh=00_AfBFFf_Dpvxafr8MJ3oBNdsDlN8PY80VlYS_dOKHCoSU_A&oe=65BF009B)  
  

You enter queries in the blank cells of the notebook. To run a query, click the play icon.

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/278392598_315887847317792_4897557074894235014_n.png?_nc_cat=105&ccb=1-7&_nc_sid=f537c7&_nc_ohc=IWgWj5JbcNMAX9ybYB0&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBdyZRLWw19weTAz07hYpqwf4BwAsLQkHYFmtCXLIxizw&oe=65BFA583)

Import the Content Library API client
-------------------------------------

All calls are made using the Content Library API Client object. You only need to import the Content Library API client once per Jupyter notebook server session.

In code block examples in this documentation, select the R or Python tab to see the corresponding code. You can copy the code and paste it into your notebook.

RPython

    library(contentlibraryapi) 
    client <- ContentLibraryAPIClient$new(version='2')

    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version = "2")

Test with a basic search
------------------------

Test your setup by running a basic search query. Here's an example to try:

RPython

    # Create a search object
    my_page_search <- client$search_pages(
        q='mountains')
            
    #Instructions for display:        
    pages <- my_page_search$query_next_page()
    print(pages)

    # Create a search object
    my_page_search = client.search_pages(
        q='mountains')
    
    #Instructions for display:
    pages = my_page_search.query_next_page()
    print(pages)

Learn more
----------

* [Jupyter](https://l.facebook.com/l.php?u=https%3A%2F%2Fjupyter.org%2F&h=AT3SIKOT2t1xBs9acD5w4yqIwSylHU37iueRWZTeswASKzm1SEfc18rwGIud389N66seF5lvIYwcE_gM0fSGv6b58UrQnWi5Dx3mZJxib1c1TFqqnsjS6JWNZr_ogZCki1t95b8M2xoHmaeG)
    
* [JupyterLab Documentation](https://l.facebook.com/l.php?u=https%3A%2F%2Fjupyterlab.readthedocs.io%2Fen%2Fstable%2F&h=AT1o67k8Wu5pxqCpFe8eReKKnyXXCMHe0oBOgPnq3Tj-N2MkJrLakPpzDJF-ucYg999SWHenIkjXP1hdIn2n4h59p_Qr8WlxVsZyYg8pJJSG_V1-gb1gGADnSbgO2rEMbLol3rbqMd497qLo)
    
* [Jupyter Notebook Basics](https://l.facebook.com/l.php?u=https%3A%2F%2Fjupyter-notebook.readthedocs.io%2Fen%2Fstable%2Fexamples%2FNotebook%2FNotebook%2520Basics.html&h=AT3XZEUwdOMWEpztm87wNfWTQJv2tf-SwV2OrXqdkfB0sGFXemuel57BE9DI6JnF-qEhqODrzvJISyzAwpxJiRIAz-9nPdai2ESOPBrTddRypu4W4I5UFc9O2PUu1gkNcnwk6C9739vBea3vuz2mbfu-0y_VKg)
    
* [Researcher Platform documentation](https://developers.facebook.com/docs/researcher-platform)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/guides
Guides
======

This section provides a guide to each of the six types of data that Meta Content Library API supports plus some additional guides to further develop your expertise with the API.

|     |     |
| --- | --- |
| ### [Facebook pages data](https://developers.facebook.com/docs/content-library-api/guide-fb-pages)<br><br>Describes the `search_pages()` method including its syntax and parameters, and some query examples. | ### [Facebook groups data](https://developers.facebook.com/docs/content-library-api/guide-fb-groups)<br><br>Describes the `search_groups()` method including its syntax and parameters, and some query examples. |
| ### [Facebook events data](https://developers.facebook.com/docs/content-library-api/guide-fb-events)<br><br>Describes the `search_events()` method including its syntax and parameters, and some query examples. | ### [Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts)<br><br>Describes the `search_posts()` method including its syntax and parameters, and some query examples. |
| ### [Instagram accounts data](https://developers.facebook.com/docs/content-library-api/guide-ig-accounts)<br><br>Describes the `search_ig_accounts()` method including its syntax and parameters, and some query examples. | ### [Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts)<br><br>Describes the `search_ig_posts()` method including its syntax and parameters, and some query examples. |
| ### [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)<br><br>Information about how search works in the Content Library API and how to create search objects. | ### [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)<br><br>Boolean operators supported by the search functionality and how to use them, including examples. |
| ### [Rate limiting and query budgeting](https://developers.facebook.com/docs/content-library-api/rate-limiting)<br><br>Rate-limiting and query-budgeting parameters for both Content Library and API. | ### [Data deletion](https://developers.facebook.com/docs/content-library-api/data-deletion)<br><br>Description of the fixed 30-day deletion schedule Meta employs. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/guide-fb-pages
Guide to Facebook Pages data
============================

You can perform Facebook Page searches by calling the Meta Content Library API client's `search_pages()` method. This document describes the `search_pages()` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-page) for detailed information about the fields that are available on a Facebook page node.

search\_pages() method
----------------------

This is the syntax of the `search_pages()` method:

search\_pages(
    q=Q,
    fields=FIELDS,    
    page\_ids=PAGE\_IDS,
    categories=CATEGORIES,
    is\_verified=IS\_VERIFIED,
    website=WEBSITE,
    admin\_countries=ADMIN\_COUNTRIES,
    since=SINCE,
    until=UNTIL
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. Searches a Page's `name` and `description` fields. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | Comma-separated list of Page fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-page) for descriptions of all available fields. |
| `PAGE_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library Page IDs as strings. Limits the query to the specified Pages. Maximum of 250 IDs. |
| `CATEGORIES`  <br>_Optional_ | List | Comma-separated list of categories to include in the search. |
| `IS_VERIFIED`  <br>_Optional_ | Boolean | The verification status of the Facebook Page. A Facebook Page with a verified badge indicates that Facebook has confirmed that it is the authentic presence for that person or brand. [Learn more](https://www.facebook.com/help/196050490547892). |
| `WEBSITE`  <br>_Optional_ | String | Website to match against the Facebook Page's "About" section. |
| `ADMIN_COUNTRIES`  <br>_Optional_ | List | Comma-separated list of countries by which to filter the Facebook Page's admin. Takes ISO Alpha-2 Country Code in 2-letter uppercase format. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook Pages created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the Page.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook Pages created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the Page.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |

Sample queries
--------------

### Search for Pages by keyword

To search for Pages that contain a specific keyword, create a search object using the `search_pages()` method with the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

RPython

    # Create a client object if you have not already done so:
    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='2')
            
    # Create a search object:
    page_search <- client$search_pages(q='cybercrime')        
    
    # No results are displayed until you provide display instructions:        
    print(page_search$query_next_page())

    # Create a client object if you have not already done so:
    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object:
    page_search = client.search_pages(q='cybercrime')
            
    # No results are displayed until you provide display instructions:
    display(page_search.query_next_page())

This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for other display and storage options.

### Request specific fields

To have the API return only specific fields on any Pages in the response, create a search object using the `search_pages()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython

    # Create a search object including a list of fields:
    page_search <- client$search_pages(q='cybercrime', fields='id,name,about')        
    
    # Specify DataFrame response format:       
    print(page_search$query_next_page('dataframe'))

    # Create a search object including a list of fields:
    page_search = client.search_pages(q='cybercrime', fields='id,name,about')
    
    # Specify DataFrame response format:        
    display(page_search.query_next_page('dataframe'))

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=3nXcV19g6AMAX9pkEeN&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDYqvuNhf4r7wLq-BYqKAWz5g9DkJb7e6Nd4tMrloKQjQ&oe=65BF473A)

### Search for Pages by Page ID

To search for Pages with specific Page IDs (obtained from the results of previous Page searches), create a search object using the `search_pages()` method with the `page_ids` parameter.

RPython

    # Create a search object limiting the response to specific Page IDs
    page_search <- client$search_pages(page_ids=['282820031228465'], fields='id,name,description')

    # Create a search object limiting the response to specific Page IDs
    page_search = client.search_pages(page_ids=['282820031228465'], fields='id,name,description')

For using Page IDs to search for posts from specific Facebook Pages, see [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts).

Learn more
----------

* [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start)
* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)
* [Data dictionary](https://developers.facebook.com/docs/content-library-api/data)
* [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)
* [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/guide-fb-groups
Guide to Facebook groups data
=============================

You can perform Facebook group searches by calling the Meta Content Library API client's `search_groups()` method. This document describes the `search_groups()` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-group) for detailed information about the fields that are available on a Facebook group node.

search\_groups() method
-----------------------

This is the syntax of the `search_groups()` method:

search\_groups(
    q=Q
    fields=FIELDS,
    group\_ids=GROUP\_IDS,
    since=SINCE,
    until=UNTIL
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | A comma-separated list of group fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-group) for descriptions of all available fields. |
| `GROUP_IDS`  <br>_Optional_ | List | A comma-separated list of Meta Content Library group IDs as strings. Limits the query to groups in the list. Maximum of 250 IDs. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook groups created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the group.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook groups created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the group.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |

Sample queries
--------------

### Search for groups by keyword

To search for public groups that contain specific keywords, create a search object using the `search_groups()` method with the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

RPython

    library(contentlibraryapi)
            
    # Create a client object if you have not already done so:
    client <- ContentLibraryAPIClient$new(version='2')
            
    # Create a search object:        
    group_search <- client$search_groups(q='cybercrime')
            
    # No results are displayed until you provide display instructions:        
    print(group_search$query_next_page())

    from contentlibraryapi import ContentLibraryAPIClient
    
    # Create a client object if you have not already done so:
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object:
    group_search = client.search_groups(q="cybercrime")
            
    # No results are displayed until you provide display instructions:
    display(group_search.query_next_page())

This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for other display and storage options.

### Request specific fields

To have the API return only specific fields on any groups in the response, create a search object using the `search_groups()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython

    # Create a search object including a list of fields:
    group_search <- client$search_groups(q='cybercrime', fields='id,name,description')        
    
    # Specify DataFrame response format:       
    print(group_search$query_next_page('dataframe'))

    # Create a search object including a list of fields:
    group_search = client.search_groups(q='cybercrime', fields='id,name,description')
    
    # Specify DataFrame response format:        
    display(group_search.query_next_page('dataframe'))

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=3nXcV19g6AMAX9pkEeN&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDYqvuNhf4r7wLq-BYqKAWz5g9DkJb7e6Nd4tMrloKQjQ&oe=65BF473A)

### Search for groups by group ID

You can search for Facebook groups using specific group IDs obtained from previous group searches.

To get data on specific Facebook groups that contain specific keywords or phrases, create a search object using the `search_groups()` method with the `q` parameter (specifying the keywords or phrases) and the `group_ids` parameter (specifying the list of group IDs you want included). If you omit the `q` argument, all groups in the list of IDs are included, not just those with a specific keyword or phrase.

RPython

    # Create a search object limiting the response to specific group IDs 
            group_search <- client$search_groups(q=`blackpink`, group_ids=[`753110959566351`], fields=`id,name,creation_date`)

    # Create a search object limiting the response to specific group IDs 
            group_search=client.search_groups(q=`blackpink`, group_ids=[`753110959566351`], fields=`id,name,creation_date`)

For using group IDs to search for posts from specific Facebook groups, see [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts).

Learn more
----------

* [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start)
* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)
* [Data dictionary](https://developers.facebook.com/docs/content-library-api/data)
* [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)
* [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/guide-fb-events
Guide to Facebook events data
=============================

You can perform Facebook event searches by calling the Meta Content Library API client's `search_events()` method. This document describes the `search_events()` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-event) for detailed information about the fields that are available on a Facebook event node.

Recurring events
----------------

Recurring events have a parent event to which all instances of the recurring event are associated by way of the `parent_event_id`. The set of fields returned for an event search differs depending on whether the event returned is a parent or an instance (child) of the recurring event. Start and end times, for example, are specific to instances of the recurring event. The following table summarizes the differences:

| Event type | Fields returned | Fields not returned |
| --- | --- | --- |
| Recurring event (the "parent" event) (event\_type=`recurring`) | `recurring_event_ids` | `attending_count`<br><br>`declined_count`<br><br>`interested_count`<br><br>`event_start_time`<br><br>`event_end_time`<br><br>`parent_event_id` |
| Instance of recurring (the "child" event) (event\_type=`instance_of_recurring`) | `attending_count`<br><br>`declined_count`<br><br>`interested_count`<br><br>`event_start_time`<br><br>`event_end_time`<br><br>`parent_event_id` | `recurring_event_ids` |

search\_events() method
-----------------------

This is the syntax of the `search_events()` method:

search\_events(
    q=Q,
    fields=FIELDS,
    event\_ids=EVENT\_IDS,
    since=SINCE,
    until=UNTIL,
    event\_since=EVENT\_SINCE,
    event\_until=EVENT\_UNTIL  
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | A comma-separated list of event fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-event) for descriptions of all available fields. |
| `EVENT_IDS`  <br>_Optional_ | List | A comma-separated list of Meta Content Library event IDs as strings. Limits the query to events in the list. Maximum of 250 IDs. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook events scheduled on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who scheduled the event.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook events scheduled on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who scheduled the event.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `EVENT_SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook events started on or after this date or timestamp are returned (used with EVENT\_UNTIL to define a time range). EVENT\_SINCE and EVENT\_UNTIL are based on UTC time zone, regardless of the local time zone of the user who started the event.<br><br>* If both EVENT\_SINCE and EVENT\_UNTIL are included, the search includes the time range defined by those values.<br>* If EVENT\_SINCE is included and EVENT\_UNTIL is omitted, the search includes the EVENT\_SINCE time through the present time.<br>* If EVENT\_SINCE is omitted and EVENT\_UNTIL is included, the search goes from the beginning of Facebook time through the EVENT\_UNTIL time.<br>* If EVENT\_SINCE and EVENT\_UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If EVENT\_SINCE and EVENT\_UNTIL are the same UNIX timestamp, the search includes the EVENT\_SINCE time through the EVENT\_SINCE time plus one hour.<br>* If EVENT\_SINCE and EVENT\_UNTIL are the same Date (YYYY-MM-DD), the search includes the EVENT\_SINCE date through the EVENT\_SINCE date plus one day. |
| `EVENT_UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook events started on or before this date or timestamp are returned (used with EVENT\_SINCE to define a time range). EVENT\_SINCE and EVENT\_UNTIL are based on UTC time zone, regardless of the local time zone of the user who started the event.<br><br>* If both EVENT\_SINCE and EVENT\_UNTIL are included, the search includes the time range defined by those values.<br>* If EVENT\_SINCE is included and EVENT\_UNTIL is omitted, the search includes the EVENT\_SINCE time through the present time.<br>* If EVENT\_SINCE is omitted and EVENT\_UNTIL is included, the search goes from the beginning of Facebook time through the EVENT\_UNTIL time.<br>* If EVENT\_SINCE and EVENT\_UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If EVENT\_SINCE and EVENT\_UNTIL are the same EVENT\_UNIX timestamp, the search includes the EVENT\_SINCE time through the EVENT\_SINCE time plus one hour.<br>* If EVENT\_SINCE and EVENT\_UNTIL are the same Date (YYYY-MM-DD), the search includes the EVENT\_SINCE date through the EVENT\_SINCE date plus one day. |

Sample queries
--------------

### Search for events by keyword

To search for public events that contain specific keywords, create a search object using the `search_events()` method with the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

RPython

    library(contentlibraryapi)
            
    # Create a client object if you have not already done so:
    client <- ContentLibraryAPIClient$new(version='2')
            
    # Create a search object:        
    event_search <- client$search_events(q='cybercrime')
            
    # No results are displayed until you provide display instructions:        
    print(event_search$query_next_page())

    from contentlibraryapi import ContentLibraryAPIClient
    
    # Create a client object if you have not already done so:
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object:
    event_search = client.search_events(q="cybercrime")
            
    # No results are displayed until you provide display instructions:
    display(event_search.query_next_page())

This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for other display and storage options.

### Request specific fields

To have the API return only specific fields on any events in the response, create a search object using the `search_events()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython

    # Create a search object including a list of fields:
    event_search <- client$search_events(q='cybercrime', fields='id,name,description')        
    
    # Specify DataFrame response format:       
    print(event_search$query_next_page('dataframe'))

    # Create a search object including a list of fields:
    event_search = client.search_events(q='cybercrime', fields='id,name,description')
    
    # Specify DataFrame response format:        
    display(event_search.query_next_page('dataframe'))

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=3nXcV19g6AMAX9pkEeN&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDYqvuNhf4r7wLq-BYqKAWz5g9DkJb7e6Nd4tMrloKQjQ&oe=65BF473A)

### Search for events by event ID

You can search for Facebook events using specific event IDs obtained from previous event searches.

To get data on specific Facebook events that contain specific keywords or phrases, create a search object using the `search_events()` method with the `q` parameter (specifying the keywords or phrases) and the `event_ids` parameter (specifying the list of event IDs you want included). If you omit the `q` argument, all events in the list of IDs are included, not just those with a specific keyword or phrase.

RPython

    # Create a search object limiting the response to specific event IDs
    event_search <- client$search_events(event_ids=['284083459792042'], fields='id,name,description,picture{url}')

    # Create a search object limiting the response to specific event IDs
    event_search = client.search_events(event_ids=['284083459792042'],  fields='id,name,creation_time')

For using event IDs to search for posts from specific Facebook events, see [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts).

Learn more
----------

* [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start)
* [Data dictionary](https://developers.facebook.com/docs/content-library-api/data)
* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)
* [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)
* [Guide to Facebook posts data](https://developers.facebook.com/docs/content-library-api/guide-fb-posts)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/guide-fb-posts
Guide to Facebook posts data
============================

You can perform Facebook post searches by calling the Meta Content Library API client's `search_posts()` method. This document describes the `search_posts()` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Jupyter notebook and have created a client object. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-post) for detailed information about the fields that are available on a Facebook post node.

search\_posts() method
----------------------

This is the syntax of the `search_posts()` method:

search\_posts(
    q=Q,
    fields=FIELDS,
    post\_ids=POST\_IDS,
    page\_ids=PAGE\_IDS,
    group\_ids=GROUP\_IDS,
    event\_ids=EVENT\_IDS,
    lang=LANG,
    link=LINK,
    is\_branded\_content=IS\_BRANDED\_CONTENT,
    admin\_countries=ADMIN\_COUNTRIES,
    owner\_types=OWNER\_TYPES,
    views\_bucket\_start=VIEWS\_BUCKET\_START,
    views\_bucket\_end=VIEWS\_BUCKET\_END
    since=SINCE,
    until=UNTIL      
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | Comma-separated list of Facebook post fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-post) for descriptions of all available fields. |
| `POST_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library post IDs as strings. Limits the query to posts in the list. Maximum of 250 IDs. |
| `PAGE_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library Page IDs as strings. Limits the query to posts from Pages in the list. Maximum of 250 IDs. |
| `GROUP_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library group IDs as strings. Limits the query to posts from groups in the list. Maximum of 250 IDs. |
| `EVENT_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library event IDs as strings. Limits the query to posts from events in the list. Maximum of 250 IDs. |
| `LANG`  <br>_Optional_ | String | The content languages of the Facebook posts to include, specified as ISO 639-1 language codes in 2-letter lowercase format. Multiple languages are comma-separated either in a single string (`lang="ru,es"`) or in an array (`lang=["ru" "es"]`). |
| `LINK`  <br>_Optional with the `q` parameter_ | String | Posts containing the specified URL are included in search results. All forms of the URL that point to the same piece of content will be returned.<br><br>  <br><br>Usage:<br><br>* Can only be used with the `q` parameter.<br>* Returns posts from exact matches only.<br>* Searching for multiple URLs in one query is not supported.<br><br>**If you want to search all posts from a domain, the `link` parameter is not the best option since it returns posts from exact matches only.**<br><br>Instead, you can use the `q` parameter where q=_url_. Results would include all posts in which the value of `q` is at least a part of the URL in the post. For example, posts from cnn.com/entertainment would be included in a search for cnn.com. Once you have the larger set of results, you can write Python or R code in your Jupyter environment to narrow them down. |
| `IS_BRANDED_CONTENT`  <br>_Optional_ | Boolean | Indicates whether the Facebook posts returned can include branded content or not. [Learn more](https://www.facebook.com/business/help/788160621327601?id=1912903575666924&content_id=OESWySYCNR5UDZX&ref=sem_smb&utm_term=dsa-1731453251743&gclid=CjwKCAjwtuOlBhBREiwA7agf1uNvtkdQIU-GlDHtOVsq1r2PAFq7Z7QFVqHPf4QsH54oi0soVculuxoCMHMQAvD_BwE). |
| `ADMIN_COUNTRIES`  <br>_Optional_ | List | Comma-separated list of countries by which to filter posts from Facebook Pages using the Page admin's country location. Only returns posts for which `owner_types = page`, whether or not the `owner_types` parameter has been set. Takes ISO Alpha-2 Country Code in 2-letter uppercase format. |
| `OWNER_TYPES`  <br>_Optional_ | List | Comma-separated list of owner types to be included in the search results. Possible values are `page`, `group` and `event`. |
| `VIEWS_BUCKET_START`  <br>_Optional_ | Integer | Facebook posts with view counts larger than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million. Used with `VIEWS_BUCKET_END` to define a range.<br><br>  <br><br>Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See [Data Dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-post) for more details. |
| `VIEWS_BUCKET_END` _Optional_ | Integer | Facebook posts with view counts smaller than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million. Used with `VIEWS_BUCKET_START` to define a range.<br><br>  <br><br>Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-fb-post) for more details. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook posts created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Facebook posts created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Facebook time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Facebook time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |

Sample queries
--------------

### Search for posts by keyword

To search for all public posts on Facebook Pages, groups, and events that contain specific keywords, create a search object using the `search_posts()` method with the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

RPython

    library(contentlibraryapi)
            
    # Create a client object if you have not already done so:
    client <- ContentLibraryAPIClient$new(version='2')
            
    # Create a search object:        
    post_search <- client$search_posts(q='cybercrime')
            
    # No results are displayed until you provide display instructions:        
    print(post_search$query_next_page())

    from contentlibraryapi import ContentLibraryAPIClient
    
    # Create a client object if you have not already done so:
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object:
    post_search = client.search_posts(q="cybercrime")
            
    # No results are displayed until you provide display instructions:
    display(post_search.query_next_page())

This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for other display and storage options.

The API only returns posts from Facebook Pages, groups, or events that can be returned on their respective endpoints (`search_pages()`, `search_groups()`, `search_events()`).

### Search for posts by post ID

To search for posts with specific post IDs (that you obtained from a previous post search), create a search object using the `search_post()` method with the `post_ids` parameter specifying a list of post IDs to include in the results.

RPython

    # Create a search object for posts with specific post IDs        
    post_search <- client$search_posts(post_ids='7069734086407812')

    # Create a search object for posts with specific post IDs
    post_search = client.search_posts(post_ids='7069734086407812')

### Search for posts from specific Facebook Pages, groups, or events

Searching for posts from specific Facebook Pages, groups, or events requires that you first obtain Page, group, or event IDs by creating search objects using the `search_pages()`, `search_groups()`, or `search_events()` methods. The search results will include the ID field by default (you don't have to specify it in your query). See [Guides](https://developers.facebook.com/docs/content-library-api/guides) to learn about these methods.

The IDs that are displayed in the search results are Meta Content Library IDs that protect user privacy and will not match the IDs of the content on Meta platforms. These Meta Content Library IDs are the ones you use in your subsequent post searches.

To search for posts from specific Pages, groups, or events, create a search object using the `search_posts()` method with the `page_ids`, `group_ids`, or `event_ids` parameter, and with or without the `q` parameter. `q` is not required but can be added to further filter posts. It does not matter when the posts were created. If you omit the `q` parameter, all public posts on the specified Pages, groups, or events are returned.

RPython

    # Create a search object for posts from specific Page IDs        
    post_search <- client$search_posts(page_ids='282820031228465')

    # Create a search object for posts from specific Page IDs
    post_search = client.search_posts(page_ids='282820031228465')

RPython

    # Create a search object for posts from specific group IDs        
    post_search <- client$search_posts(group_ids='634974087068385')

    # Create a search object for posts from specific group IDs
    post_search = client.search_posts(group_ids='634974087068385')

RPython

    # Create a search object for posts from specific event IDs        
    post_search <- client$search_posts(event_ids='1025592588867344')

    # Create a search object for posts from specific event IDs
    post_search = client.search_posts(event_ids='1025592588867344')

RPython

    # Create a search object that combines searching for posts from specific Page IDs and specific group IDs       
    post_search <- client$search_posts(page_ids='282820031228465', group_ids='634974087068385')

    # Create a search object that combines searching for posts from specific Page IDs and specific group IDs 
    post_search = client.search_posts(page_ids='282820031228465', group_ids='634974087068385')

### Request specific fields

To have the API return only specific fields on any Facebook posts in the response, create a search object using the `search_posts()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython

    # Create a search object including a list of fields:
    post_search <- client$search_posts(q='cybercrime', fields='id,text,lang')        
    
    # Specify DataFrame response format:       
    print(post_search$query_next_page('dataframe'))

    # Create a search object including a list of fields:
    post_search = client.search_posts(q='cybercrime', fields='id,text,lang')
    
    # Specify DataFrame response format:        
    display(post_search.query_next_page('dataframe'))

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=3nXcV19g6AMAX9pkEeN&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDYqvuNhf4r7wLq-BYqKAWz5g9DkJb7e6Nd4tMrloKQjQ&oe=65BF473A)

### Search for Facebook posts containing a specific URL

To search for all public posts on Facebook Pages, groups, and events that contain specific keywords and a specific URL, create a search object using the `search_posts()` method with the `q` and `link` parameters. The `link` parameter cannot be used without the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

All forms of the URL that point to the same piece of content will be returned. Searching for multiple URLs in one query is not supported.

RPython

    # Create a search object including both the `q` and `link` parameters:
            
    post_search <- client$search_posts(q="nike", link="nike.com")
    print(post_search$query_next_page('dataframe'))

    # Create a search object including both the `q` and `link` parameters:
            
    post_search = client.search_posts(q="nike", link="nike.com")
    display(post_search.query_next_page('dataframe'))

Including multimedia in search results: Third-party cleanroom environment only
------------------------------------------------------------------------------

If you are using the Meta Content Library API in an approved third-party cleanroom environment (as opposed to Meta's Researcher Platform), _and if that environment supports it_, you have the option of including multimedia (photo, video) in your search results. Multimedia in posts from Facebook Pages, groups, and events are all eligible.

* Include the keyword `multimedia` in your query (`fields` parameter).
    
* For any media contained in a post, the response will include the type of media (photo, video), an ID, and either the media itself or a link to where the cleanroom environment has stored the media. Whether the media can be displayed directly in the response or not depends on the third-party cleanroom interface.
    
* The number of calls allowed that include multimedia is controlled by a multimedia query budget specific to the third-party cleanroom environment. See [Rate limiting and query budgeting for multimedia](https://developers.facebook.com/docs/content-library-api/rate-limiting#multimedia-query-limit) for more information.
    

Learn more
----------

* [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start)
* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)
* [Data dictionary](https://developers.facebook.com/docs/content-library-api/data)
* [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)
* [Rate limiting and query budgeting for multimedia](https://developers.facebook.com/docs/content-library-api/rate-limiting#multimedia-query-limit)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/guide-ig-accounts
Guide to Instagram accounts data
================================

You can perform searches for Instagram creator, business, and certain personal accounts by calling the Meta Content Library API client's `search_ig_accounts()` method.

For personal accounts, only those that have account privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT07vXMxIWruG0ty60Iv36MZ5K8q6gRPHWRWmm2xDePX7SLoU8VJzyP4TuwlkRVspGtLV6Qwya5mtIvQQgnNuRRhvwhmWdnsu_HyPpimv4rmdDADR1W8PwHuXNL3KZW7PBWKpKs97lG8k5uf), and have either a [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT2-FmhBrURs62X-uOb58Y5x96_t6l4vX_YcMm3Vtcq7oMh9Us1f-QY8RpAR_3I39ZARALrVF5l9RsCbBDe7B0FAPeqpR7k8Nl_HrKBAKVQQgJWf_KTPaYXQ43zD7yUzGmEmbSFCN0k3f6m9) or 50,000 or more followers are included. This document describes the \`search\_ig\_accounts()\` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Python or R Jupyter notebook and have created a client object. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-account) for detailed information about the fields that are available on an Instagram account node.

search\_ig\_accounts() method
-----------------------------

This is the syntax of the `search_ig_accounts()` method:

search\_ig\_accounts(
    q=Q,
    fields=FIELDS,
    account\_ids=ACCOUNT\_IDS,
    account\_types=ACCOUNT\_TYPES,
    is\_verified=IS\_VERIFIED,
    since=SINCE,
    until=UNTIL      
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search Instagram accounts for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | A comma-separated list of Instagram account fields you want included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-account) for descriptions of all available fields. |
| `ACCOUNT_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library Instagram account IDs to include in the search results. Maximum of 250 IDs. |
| `ACCOUNT_TYPES`  <br>_Optional_ | List | Comma-separated list of account types of the Instagram accounts to be included in the search results. Possible values are `creator`, `business` and `personal`.<br><br>Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT35bM9jd4-51bPM-dSx0NBJ961SaJNjMPeCdTU2npg_1CV6LhbLtdivmsIlJsSZygReOQ2hbgRzyF1mG8E_ZSLuKhptc5GoTX2Afkm8UAJ33kpGXNxfejtSF7-gGQB_v_kqpsQo3zRjMwqz) and have either a verified badge or 50,000 or more followers. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT2wLuUfIfonVYEVbqVIxC1ig3EpytHQpIi4qNKY0UHz-vM5tm555Vtx7rgpIO5sFjSpX3nZ_kv2Hg_mA0m-JniKL_vBJ8XMMGXe8JKlsmmhYi3vpVZl1nuhfUC20yhNE1ORraGgX53--elS) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. |
| `IS_VERIFIED`  <br>_Optional_ | Boolean | Whether the Instagram account is verified. An Instagram account with a legacy blue verified badge means that Instagram has confirmed that it is the authentic presence for that person or brand. [Learn more](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F854227311295302&h=AT2g_GUGNTO7wifBolL_vycelEy3jnLBcSLWKwNJ8cp2x-FtnD1dwpJEcBgWFTDXOSfS_H86rupzk4rsM_jo6Bz4F1UnyF4zJbanhaVWrK7y48h3gzgumjI5pvVLPz67DkcxqH7hnOVhVjFu). |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram accounts created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the account.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram accounts created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who created the account.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |

Sample queries
--------------

### Search for Instagram accounts by keyword

To search for Instagram accounts that contain a specific keyword, create a search object using the `search_ig_accounts()` method with the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

RPython

    # Create a client object if you have not already done so:
    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='2')
            
    # Create a search object:
    ig_account_search <- client$search_ig_accounts(q='cybercrime')        
    
    # No results are displayed until you provide display instructions:        
    print(ig_account_search$query_next_page())

    # Create a client object if you have not already done so:
    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object:
    ig_account_search = client.search_ig_accounts(q='cybercrime')
            
    # No results are displayed until you provide display instructions:
    display(ig_account_search_search.query_next_page())

This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for other display and storage options.

### Request specific fields

To have the API return only specific fields on any Instagram accounts in the response, create a search object using the `search_ig_accounts()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython

    # Create a search object including a list of fields:
    ig_account_search <- client$search_ig_accounts(q='cybercrime', fields='id,name,biography')        
    
    # Specify DataFrame response format:       
    print(ig_account_search$query_next_page('dataframe'))

    # Create a search object including a list of fields:
    ig_account_search = client.search_ig_accounts(q='cybercrime', fields='id,name,biography')
    
    # Specify DataFrame response format:        
    display(ig_account_search.query_next_page('dataframe'))

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=3nXcV19g6AMAX9pkEeN&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDYqvuNhf4r7wLq-BYqKAWz5g9DkJb7e6Nd4tMrloKQjQ&oe=65BF473A)

### Search for Instagram accounts by account ID

You can search for Instagram accounts using specific account IDs obtained from previous account searches.

To get data on specific Instagram accounts that contain specific keywords or phrases, create a search object using the `search_ig_accounts()` method with the `q` parameter (specifying the keywords or phrases) and the `account_ids` parameter (specifying the list of account IDs you want included). If you omit the `q` argument, all accounts in the list of IDs are included, not just those with a specific keyword or phrase.

RPython

    # Create a search object limiting the response to specific account IDs 
            account_search <- client$search_ig_accounts(q=`fifa`, account_ids=[`315242517956050`], fields=`id,name,creation_date`)

    # Create a search object limiting the response to specific account IDs 
            account_search=client.search_ig_accounts(q=`fifa`, account_ids=[`315242517956050`], fields=`id,name,creation_date`)

For using Instagram account IDs to search for posts from specific Instagram accounts, see [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts).

Learn more
----------

* [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start)
* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)
* [Data dictionary](https://developers.facebook.com/docs/content-library-api/data)
* [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)
* [Guide to Instagram posts data](https://developers.facebook.com/docs/content-library-api/guide-ig-posts)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/guide-ig-posts
Guide to Instagram posts data
=============================

You can perform searches for Instagram posts from public Instagram creator, business, and a subset of personal accounts by calling the Meta Content Library API client's `search_ig_posts()` method.

Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT1kMMNbwTabLwbZHs52apB3Cz3CknBf53XMxF49QYYHRdbAB-9lk8gaIw5qI3S2BuvWq4zt_q4_4zgau_jsofnJT4schF1BpRXSOSn58DKd66sKL6rsyx-Hklz5hk9UAneEJnm8ikmnNr_J) and have either a verified badge or 50,000 or more followers. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT2gWNSoCC5XSFudCGbDRbWLeguZVjLhpBRF7WGmo3V1Q51-qtD7GW9Y8ipAGQLjk_Ak6e_oHtI0ufpRBlcEJfHnWEEwfXcgO9eZTexJXMkLvXB5ZMucutiaquWsPnvbBSXI7HSizswXPuUx) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription.

This document describes the `search_ig_posts()` method and its syntax and parameters, and shows how to perform basic queries using the method.

All of the examples in this document assume you have already created a Jupyter notebook and have created a client object. See [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) to learn more.

See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-post) for detailed information about the fields that are available on an Instagram post node.

search\_ig\_posts() method
--------------------------

This is the syntax of the `search_ig_posts()` method:

search\_ig\_posts(
    q=Q,
    fields=FIELDS,
    post\_ids=POST\_IDS,
    account\_ids=ACCOUNT\_IDS,
    account\_types=ACCOUNT\_TYPES,
    lang=LANG,
    is\_branded\_content=IS\_BRANDED\_CONTENT,
    media\_types=MEDIA\_TYPES,
    views\_bucket\_start=VIEWS\_BUCKET\_START,
    views\_bucket\_end=VIEWS\_BUCKET\_END
    since=SINCE,
    until=UNTIL  
)

The following table describes the parameters:

| Parameter | Type | Description |
| --- | --- | --- |
| `Q`  <br>_Optional_ | String | Keyword(s) to search for. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches with Boolean operators are handled. |
| `FIELDS`  <br>_Optional_ | List | Comma-separated list of Instagram post fields to be included in search results. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-post) for descriptions of all available fields. |
| `POST_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library post IDs to include in search results. Limits the query to posts in the list. Maximum of 250 IDs. |
| `ACCOUNT_IDS`  <br>_Optional_ | List | Comma-separated list of Meta Content Library account IDs as strings. Limits the query to posts from accounts in the list. Maximum of 250 IDs. |
| `ACCOUNT_TYPES`  <br>_Optional_ | List | Comma-separated list of Instagram account types. Possible values are `creator`, `business`, and `personal`.<br><br>Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT3QoL3W6TXSG-rxoFyWdvY1FWS2zX5Xi7-blR4fL0-AkeYXErMTqxi0khY6KKm4ju5_nQl73xB8cXV6cQ3bjaKN206RrM9HiqoBjKgtOT2z-5Gfvjbqw3zRUreHEMIQq3f7xMDJkHDkq9wlaKIr2tXBOjNgBQ) and have either a verified badge or 50,000 or more followers. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT20UeaFdNTDQxXvreLoOj6SY6ueVf9hJdJUXdfPJgkJofAasKbFZkYJXWYeTkj6ycgymUOwqoi2ZmYMs2MRq8IZo6nnv0KzjlzikTeISTfwpX5scYGC76DT-djT4LTM2Sa7cJwVfdHKnCmY) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. |
| `LANG`  <br>_Optional_ | String | The content languages of the Instagram posts to include, specified as ISO 639-1 language codes in 2-letter lowercase format. Multiple languages are comma-separated either in a single string (`lang="ru,es"`) or in an array (`lang=["ru" "es"]`). |
| `IS_BRANDED_CONTENT`  <br>_Optional_ | Boolean | Indicates whether the Instagram posts returned can include branded content or not. [Learn more](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1123581461537025%2F%3Fhelpref%3Dsearch%26query%3Dbrand%2520content%26search_session_id%3Df7d00d14670ab93e032d827b36e54ff3%26sr%3D1&h=AT3fwepWxJp-cxYUp1rxlOH0M0J21ye4eITf4G1b2tT4ngh7Em3ufO4_NkYnl6MIDc_15Y1cBlzQ7uf70E1yNydCP9-d0qx7odBmkw055rxEEJFaSH0QeZoVlUGZRtx7abJn8j8fWyv2P7kh). |
| `MEDIA_TYPES`  <br>_Optional_ | List | Comma-separated list of media types to be included in the search results. Media types include `albums`, `photos`, and `videos` (including reels). |
| `VIEWS_BUCKET_START`  <br>_Optional_ | Integer | Instagram posts with view counts larger than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million.<br><br>  <br><br>Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-post) for more details. |
| `VIEWS_BUCKET_END`  <br>_Optional_ | Integer | Instagram posts with view counts smaller than or equal to this number match the search criteria. Range is from 0 to the maximum of more than 100 million.<br><br>  <br><br>Views are the number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. See [Data dictionary](https://developers.facebook.com/docs/content-library-api/data#dd-ig-post) for more details. |
| `SINCE`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram posts created on or after this date or timestamp are returned (used with UNTIL to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |
| `UNTIL`  <br>_Optional_ | String or Integer | Date in YYYY-MM-DD (date only) or UNIX timestamp (translates to a date and time to the second) format. Instagram posts created on or before this date or timestamp are returned (used with SINCE to define a time range). SINCE and UNTIL are based on UTC time zone, regardless of the local time zone of the user who made the post.<br><br>* If both SINCE and UNTIL are included, the search includes the time range defined by those values.<br>* If SINCE is included and UNTIL is omitted, the search includes the SINCE time through the present time.<br>* If SINCE is omitted and UNTIL is included, the search goes from the beginning of Instagram time through the UNTIL time.<br>* If SINCE and UNTIL are both omitted, the search goes from the beginning of Instagram time to the present time.<br>* If SINCE and UNTIL are the same UNIX timestamp, the search includes the SINCE time through the SINCE time plus one hour.<br>* If SINCE and UNTIL are the same Date (YYYY-MM-DD), the search includes the SINCE date through the SINCE date plus one day. |

Sample Queries
--------------

### Search for Instagram posts by keyword

To search for all public posts from public Instagram accounts that contain a specific keyword, create a search object using the `search_ig_posts()` method with the `q` parameter. See [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search) for information about how multiple keyword searches are handled.

RPython

    library(contentlibraryapi)
    
    # Create a client object if you have not already done so:
    client <- ContentLibraryAPIClient$new(version='2')
            
    # Create a search object:        
    ig_post_search <- client$search_ig_posts(q='cybercrime')
            
    # No results are displayed until you provide display instructions:        
    print(ig_post_search$query_next_page())

    from contentlibraryapi import ContentLibraryAPIClient
    
    # Create a client object if you have not already done so:
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object:
    if_post_search = client.search_ig_posts(q="cybercrime")
            
    # No results are displayed until you provide display instructions:
    display(ig_post_search.query_next_page())

This example would return only 10 results per page. You can keep calling `query_next_page()` to get the next page of 10 results, until all the search results have been returned. See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for other display and storage options.

The API only returns posts from Instagram accounts that can be returned from the `search_ig_accounts` endpoint.

### Request specific fields

To have the API return only specific fields on any Instagram posts in the response, create a search object using the `search_ig_posts()` method with the `fields` parameter and a comma-separated list of fields you want included. If omitted, default fields will be returned. To more easily see columns of data, this example specifies a DataFrame response format (the default response format is JSON).

RPython

    # Create a search object including a list of fields:
    ig_post_search <- client$search_ig_posts(q='cybercrime', fields='id,text,creation_time')        
    
    # Specify DataFrame response format:       
    print(ig_post_search$query_next_page('dataframe'))

    # Create a search object including a list of fields:
    ig_post_search = client.search_ig_posts(q='cybercrime', fields='id,text,creation_time')
    
    # Specify DataFrame response format:        
    display(ig_post_search.query_next_page('dataframe'))

DataFrame response format has clear columns:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/361588460_224466613889350_7431544641123459816_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=3nXcV19g6AMAX9pkEeN&_nc_ht=scontent-cdg4-3.xx&oh=00_AfDYqvuNhf4r7wLq-BYqKAWz5g9DkJb7e6Nd4tMrloKQjQ&oe=65BF473A)

### Search for posts by post ID

To search for posts with specific post IDs (that you obtained from a previous post search), create a search object using the `search_ig_posts()` method with the `post_ids` parameter specifying a list of post IDs to include in the results.

RPython

    # Create a search object for posts with specific post IDs        
    post_search <- client$search_ig_posts(post_ids='7069734086407812')

    # Create a search object for posts with specific post IDs
    post_search = client.search_ig_posts(post_ids='7069734086407812')

### Search for posts from specific Instagram accounts

Searching for posts from specific Instagram accounts requires that you first obtain account IDs by creating a search object using the `search_ig_accounts()` method. The search results will include the ID field by default (you don't have to specify it in your query). See [Guide to Instagram accounts data](https://developers.facebook.com/docs/content-library-api/guide-ig-accounts) to learn about this method.

The IDs that are displayed are Meta Content Library IDs that protect user privacy and will not match the IDs of the content on Meta platforms. These Meta Content Library IDs are the ones you use in your subsequent post searches.

To search for posts from specific accounts, create a search object using the `search_ig_posts()` method with the `account_ids` parameter, and with or without the `q` parameter. `q` is not required but can be added to further filter posts. It does not matter when the posts were created. If you omit the `q` parameter, all public posts from the specified accounts are returned.

RPython

    # Create a search object for posts from specific account IDs        
    post_search <- client$search_ig_posts(account_ids='315242517956050')

    # Create a search object for posts from specific account IDs
    post_search = client.search_ig_posts(account_ids='315242517956050')

Including multimedia in search results: Third-party cleanroom environments only
-------------------------------------------------------------------------------

If you are using the Meta Content Library API in an approved third-party cleanroom environment (as opposed to Meta's Researcher Platform), _and if that environment supports it_, you have the option of including multimedia (photo, video) in your search results. Multimedia in posts from Instagram business, creator, and personal accounts are all eligible.

* Include the keyword `multimedia` in your query (`fields` parameter).
    
* For any media contained in a post, the response will include the type of media (photo, video), an ID, and either the media itself or a link to where the cleanroom environment has stored the media. Whether the media can be displayed directly in the response or not depends on the third-party cleanroom interface.
    
* The number of calls allowed that include multimedia is controlled by a multimedia query budget specific to the third-party cleanroom environment. See [Rate limiting and query budgeting for multimedia](https://developers.facebook.com/docs/content-library-api/rate-limiting#multimedia-query-limit) for more information.
    

Learn more
----------

* [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start)
* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)
* [Data dictionary](https://developers.facebook.com/docs/content-library-api/data)
* [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)
* [Guide to Instagram accounts data](https://developers.facebook.com/docs/content-library-api/guide-ig-accounts)
* [Rate limiting and query budgeting for multimedia](https://developers.facebook.com/docs/content-library-api/rate-limiting#multimedia-query-limit)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/guide-search-object
Search guide
============

How search works
----------------

Queries in Meta Content Library and API are powered by a version of Facebook’s [search engine infrastructure](https://research.facebook.com/publications/unicorn-a-system-for-searching-the-social-graph/), which relies on a combination of indexing and ranking to return relevant entities. The retrieval function combines matched and ranked IDs from a query using the same distributed [memory caching layer](https://l.facebook.com/l.php?u=https%3A%2F%2Fengineering.fb.com%2F2013%2F06%2F25%2Fcore-data%2Ftao-the-power-of-the-graph%2F&h=AT1qjsyCfu7oKiwR7oD7250UOC5Sd14-ieuau-hKBvw8ihrsyVgrnEgA0EB9a_P6uYFJFNOtPDFvwp5XPqKRPkspRQg7-voKD0v2hAJAWWG2DdAxIJgw4c8v7VKsYunYv4TY1O3S3PkQSrHM) which serves live platform content. This ensures that results represent the most current state of content on the platform and meet privacy-preserving visibility criteria (see [Frequently asked questions](https://developers.facebook.com/docs/content-library-api/disclosures) for details).

As content is created or modified on Meta platforms, associated entities are registered to a search index built from individual words extracted from text fields as _tokens_. Tokenization generally isolates words separated by spaces or punctuation ( ?@$%^\*()+=~\[{}\];:"<>|. ), with some URL normalization and locale-specific adjustments for non-English languages. Tokenization is exact, in that it does not introduce additional word variants ("cats" will not be tokenized to "cat"). Direct mentions of users or other platform entities (via @) are not tokenized and are scrubbed from returned text fields, and are thus not searchable.

At query time, relevant content is identified by exact matching between tokens and individual search terms. Candidate matches are then subject to additional filtering via Boolean query logic (see [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)) and other selected filters. Matching is performed independently by word in a query, meaning that searching by phrase is not supported (queries “All for one” and “One for all” are equivalent).

Search objects in the API
-------------------------

The Content Library API uses search objects to extract a subset of data from an extremely large online database. Each search object specifies the search method to be used and sets the values of the parameters that determine which data will be returned.

The parameters accepted by each search method are described in the search method [guides](https://developers.facebook.com/docs/content-library-api/guides).

The following sections describe how to use search objects to achieve various objectives, providing query examples in both R and Python.

* [Basic synchronous search with paginated results](#sync-search)
    
* [Response formats](#res-formats)
    
* [Altering search parameters](#alter-search)
    
* [Asynchronous search](#async-search)
    
* [Estimating response size](#estimate)
    

### Basic synchronous search with paginated results

Unless you specify otherwise, a search object is synchronous in nature, meaning that you submit the query and wait for the results, and you cannot submit another until the first one finishes. Synchronous search results display 10 results at a time (a "page") and you request the next pages one by one. This type of search is most useful when the data matching the search criteria is expected to be small or when you just want to sample some results to see if they are appropriate for your research and don't necessarily need to see everything. This can be a step in the process of fine-tuning your search criteria.

Synchronous searches can return a maximum of 1000 results. When you need a larger set of results, use [asynchronous searches](#async-search).

RPython

    #Import the client library if you have not already done so:        
    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='2')
    
    # Create a search object using the search_posts() search method:
    post_search <- client$search_posts(
        q='mountains',
        since=1622937600,
        until=1686095999)
            
    # Instructions for display:        
    posts <- post_search$query_next_page()
    print(posts)

    #Import the client library if you have not already done so:
    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    # Create a search object using the search_posts() search method:
    post_search = client.search_posts(
        q='mountains',
        since=1622937600,
        until=1686095999)
            
    #Instructions for display:        
    posts = post_search.query_next_page()
    print(posts)

### Response formats

By default, search responses use JavaScript Object Notation (JSON) format. This response format uses separators rather than being organized into columns. If you prefer the display in columns, the API has a function to specify DataFrame format instead.

RPython

    # Create a search object
    post_search <- client$search_posts(
        q='mountains')
            
    # Instructions for display:        
    print(post_search$query_next_page('dataframe'))

    # Create a search object
    post_search = client.search_posts(
        q='mountains')
    
    #Instructions for display:
    
    display(post_search.query_next_page('dataframe'))

### Altering search parameters

While exploring the data to arrive at the most appropriate search parameters for your purposes, you might find the `alter_search_params` method useful. This method returns a new search object with any new parameters you specify overriding the original ones.

RPython

    # Get a new search object with altered parameters:
    new_post_search <- post_search$alter_search_params(q = 'mountains', lang='en,es', since=1622937600,
        until=1622938000)
    
    # Instructions for display:
    new_post <- new_post_search$query_next_page()
    print(new_post)

    # Get a new search object with altered parameters:
    new_post_search = post_search.alter_search_params(q = 'mountains', lang='en,es', since=1622937600,
        until=1622938000)
    
    # Instructions for display:
    new_post = new_post_search.query_next_page()
    print(new_post)

### Asynchronous search

Asynchronous searching capability is available for when you want to work with all of the data returned from a search, up to the search results limit that applies to every individual asynchronous search. Asynchronous searches can take some time (minutes to days) to complete because they return all of the data requested, not just one page at a time. However, because the search happens in the background, you don't have to wait for the results before submitting another search or doing other work. Once the search results are ready, you can fetch them.

The search result limit for each asynchronous search is 100,000 results. See [Estimating response size](#estimate).

Researcher Platform also has an asynchronous search feature, but that is strictly for static database use and does not work the same way. With Content Library API, you can only use the `async_search()` method described here.

When you submit an asynchronous search, the API returns "True" indicating the successful submission of the asynchronous query if the expected results are below the 100,000 search results limit, and an error message if the expected results are over the limit.

If the search is successfully submitted, you can check on the status and receive either IN\_PROGRESS or COMPLETE.

Use the `submit_async_query()` method with `async_status`:

RPython

    # Previous example submitted as an async search:
    async_submission <- new_post_search$submit_async_query()
    print(async_submission) # Returns True or error
    
    async_status <- new_post_search$get_async_search_status()
    print(async_status) # ex: # Returns IN_PROGRESS or COMPLETE

    # Previous example submitted as an async search:
    async_submission = new_post_search.submit_async_query()
    print(async_submission) # Returns "True" or an error
    
    async_status = new_post_search.get_async_search_status()
    print(async_status) # Returns IN_PROGRESS or COMPLETE

When the check for status shows COMPLETE, you can fetch the data in either JSON or DataFrame format (JSON is the default). You can also write the data to a file, which will be stored in the `/previous_searches/` folder in your Jupyter environment in JSON format.

RPython

    data <- new_post_search$get_data("dataframe") # Specifies DataFrame format
            
    new_post_search$write_data_to_file("file_name")  # Writes data to a file

    data = new_post_search.get_data("dataframe") # Specifies DataFrame format
            
    new_post_search.write_data_to_file("file_name") # Writes data to a file

Use the `get_all_async_queries()` method to get a list of all your previously executed asynchronous searches.

RPython

    # Get a list of search objects you've previously executed asynchronously:
    previous_searches <- client$get_all_async_queries()

    # Get a list of Search objects you've previously executed asynchronously:
    previous_searches = client.get_all_async_queries()
    print(previous_searches)

### Estimating response size

Use the `get_estimate()` function to get a rough idea of how much data would be returned from a search you have defined. Since the API can only return up to 100,000 results from a single asynchronous search, it can be helpful to know in advance if your search is likely to fail because the response size is too large. If the estimate comes out higher than 100,000, consider modifying the parameters to reduce the response size. You can continue to modify the search parameters and get new estimates until the search results are predicted to fall below the maximum allowed.

This is typically most useful for post searches because the number of results tend to be higher, but it can be used to estimate the size of data that would be returned by any search.

RPython

    # Request an estimate:
    post_search <- client$search_posts(q = 'dogs')
    estimate <- post_search$get_estimate()
            
    # Display the estimate:        
    print(estimate)

    # Request an estimate:  
    post_search = client.search_posts(q='dogs')
    estimate = post_search.get_estimate()
          
    # Display the estimate:        
    print(estimate)

Learn more
----------

* [Rate limiting and query budgeting](https://developers.facebook.com/docs/content-library-api/rate-limiting)
* [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)
* [Search quality approach](https://developers.facebook.com/docs/content-library-api/search-quality)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/adv-search
Advanced search guidelines
==========================

Meta Content Library and API have a search functionality that supports AND, OR, and NOT operators. Query strings are passed as the `q` parameter as in this example (select the tab for the language of your choice):

RPython

    response <- client$search_posts(q=“dogs | cats & pets”)

    response = client.search_posts(q=“dogs | cats & pets”)

General rules
-------------

The following general rules apply to forming queries:

* The following operators are supported: AND, OR, NOT.
* Use an ampersand character (&) or a blank space to indicate AND.
* Use a pipe character ( | ) to indicate OR.
* Use a hyphen character (-) to indicate NOT. The en-dash and em-dash characters are _not_ interpreted as substitutes for hyphen and are treated instead as keywords.
* For queries with multiple operators, NOT clauses are processed first, followed by AND, followed by OR. Imagine the terms grouped as if with parentheses.
* For clauses of equal precedence, there is a default left-to-right processing order.
* Grouping using parentheses is supported. Grouping can be used to modify the default processing order.
* You can use single-word keywords only (not phrases).
* Wild cards are not supported.
* Extra spaces around operators are ignored, so you can have them or not.

Because they have special meaning in the context of query syntax, the following characters cannot be used as keywords or embedded in keywords:

* & ampersand
* | pipe
* ‐ hyphen
* space
* ( open parenthesis
* ) close parenthesis

Using operators
---------------

The examples included here demonstrate the basic use of the AND, OR, and NOT operators.

| Search objective | How to write it | Examples |
| --- | --- | --- |
| Find matches that include all of the provided search terms. | Use the AND operator expressed as an ampersand character (&) or a blank space. | cat&dog&allergy<br><br>cat dog allergy<br><br>cat&dog allergy<br><br>cat dog&allergy<br><br>  <br><br>Each match contains all three terms: “cat”, “dog”, and “allergy”. |
| Find matches that include at least one of the provided search terms. | Use the OR operator expressed as a pipe character (\|). | cat \| dog<br><br>cat\|dog<br><br>cat \|dog<br><br>cat\| dog<br><br>  <br><br>Each match contains “cat” or “dog”, and could contain both. |
| Find matches that include the provided search term, excluding a second term. | Use the NOT operator expressed as a hyphen character (-). | dog -puppy<br><br>dog-puppy<br><br>dog- puppy<br><br>dog - puppy<br><br>  <br><br>Each match contains “dog” but not “puppy”. Results containing both “dog” and “puppy” are excluded. |

Multiple operators
------------------

When multiple operators are included in a single query string, the operators are processed (parsed) in a specific order: NOT first, followed by AND, followed by OR. This is important to understand because it means the order in which you place the operators in your query might be different from the order in which they are parsed, which might or might not affect the results.

The examples in this section demonstrate the use of multiple operators in a single query.

| Search objective | How to write it | Examples |
| --- | --- | --- |
| Find matches that include both of two search terms (AND clause), as well as matches that include a third term (OR clause). | Use both an AND clause and an OR clause. The AND clause is parsed first. | lemon lime \| grapefruit<br><br>grapefruit \| lemon lime<br><br>  <br><br>Results include matches containing both “lemon” and “lime”, plus those containing “grapefruit”. |
| Find:<br><br>1. Matches that contain one search term, excluding those containing a second term, and<br>    <br>2. Matches that contain a third term<br>    <br><br>**Note**: Some matches might meet both criteria 1 and 2, but to be included in the query results, the only requirement is to match at least one. | Use both a NOT clause and an OR clause. The NOT clause is parsed first. | fuyu \| persimmon - astringent<br><br>persimmon - astringent \| fuyu<br><br>  <br><br>Results include:<br><br>1. Matches containing “persimmon” but not “astringent” (imagine persimmon - astringent grouped as if in parentheses), and<br>    <br>2. Matches containing “fuyu”<br>    <br><br>Some matches might contain “persimmon” but not “astringent” and also contain “fuyu” (matching both 1 and 2 above), but this is not a requirement to be included in the query results.<br><br>  <br><br>**Note**: If you actually want to exclude “astringent” from “fuyu” as well, you could achieve that using grouping, a technique for customizing the order of precedence. See the next section on [Grouping](#grouping-section). |

Grouping
--------

You can use grouping with parentheses to influence the order in which clauses are parsed. Clauses enclosed in parentheses are parsed first, followed by operators outside of parentheses.

The examples shown here demonstrate how this works.

| Search objective | How to write it | Examples |
| --- | --- | --- |
| Find matches that contain at least one of two search terms, excluding those that also contain a third term. | Use an OR clause enclosed in parentheses to ensure it is parsed first, followed by a NOT clause. Without the parentheses, the NOT clause would be parsed first. | (fuyu \| persimmon) - astringent<br><br>  <br><br>Results include matches containing either “fuyu” or “persimmon” (or both), but exclude those that also contain “astringent”. |
| Find matches that contain both of two search terms or at least one of two other search terms. Exclude from that list all results that also contain a fifth search term. | Use an AND clause in parentheses, and an OR clause in parentheses. Separate the two parenthetical clauses by an OR operator. Group those two groupings together. Finally, add the NOT clause.<br><br>  <br><br>The extra grouping ensures that "outlaw" is not excluded only from the (newman \| redford) results, but also from the (action movie) results. | ((action movie) \| (newman \| redford)) - outlaw<br><br>  <br><br>Results:<br><br>* Include matches containing both “action” and “movie”<br>* Include matches containing either “newman” or “redford” (can contain both)<br>* Exclude matches that also contain “outlaw” |

Right-to-left languages
-----------------------

A few notes about queries when applied to languages that are read right to left:

* Query logic for right-to-left languages is parsed right to left
* The parsing order (NOT followed by AND followed by OR) is maintained
* Grouping is not supported for right-to-left languages

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/rate-limiting
Rate limiting and query budgeting
=================================

Meta Content Library and API both have limits at the individual researcher level that:

* Put a cap on the number of queries allowed per user per minute (a separate limit for each tool). This is called a _rate limit_.
    
* Put a cap on the number of retrieved data records (posts, for example) per user per seven-day rolling window. This limit, called a _query budget_, is shared between the two tools per user. In other words, a single researcher has a total query budget between the two tools, regardless if they are using just Content Library, just Content Library API, or both.
    

Maintaining a rate-limiting and query-budgeting policy ensures that the tools run efficiently and provide all users with consistent data access, unhindered by reduced performance. It also provides a measure of protection against system flooding.

What are the limits?
--------------------

### Rate limits for Content Library

* 60 queries over any one-minute interval

### Rate limits for Content Library API

* Synchronous search queries: 60 queries over any one-minute interval
    
* Asynchronous search queries: 1 query per minute
    

See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for information about the difference between synchronous and asynchronous searches.

### Combined query budget per researcher

For Content Library and API combined, you can retrieve a maximum of 500,000 data records per seven-day rolling window. The rolling window is one week previous to the current timestamp (to the second). If you are blocked by hitting the query budget, you should not need to wait long before you try again.

If you are using the Content Library API in a third-party cleanroom environment, and if that environment supports including multimedia in posts, there is an additional query budget of 1000 queries with multimedia per rolling week.

How to request a limit increase
-------------------------------

If you have questions or concerns about the impact of your limits on your research, contact us through [Direct Support](https://developers.facebook.com/docs/content-library-and-api/direct-support).

Limit reached messaging
-----------------------

### Content Library

Content Library warns you when you get close to the maximum number of data records retrieved per seven-day rolling window (query budget) with a banner at the top of the page. This is an example of what the banner looks like:

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/367743972_262423759986978_211809594479650483_n.png?_nc_cat=102&ccb=1-7&_nc_sid=f537c7&_nc_ohc=jsN-z2cH3YYAX-3c11L&_nc_ht=scontent-cdg4-1.xx&oh=00_AfAh6CHmWAq6-6uoaRmc5rrYfsBX94-1-abvRnynIms66A&oe=65BF5964)

When you reach your query budget, you will see a different banner at the top of the page that looks like this:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/367729115_698453068806558_1327188573085519935_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=nKpmcd2YsUoAX9oe-fw&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAdyEBW3zDyv1y9YRT-MMh5UWdSDEbKrZJXa0paGoF02A&oe=65BEBBA9)

The banner has a "Learn more" link, which will open the following message with additional details about rate limits:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/367733689_3623192734669772_7188247576546648393_n.png?_nc_cat=104&ccb=1-7&_nc_sid=f537c7&_nc_ohc=XOMdupwPXaAAX9j40ZS&_nc_ht=scontent-cdg4-3.xx&oh=00_AfA2Nj0WCJ6kluo-nZubUEDJgmOlLzAB6J8X9qX5RxCDFg&oe=65BE4BD5)

### Content Library API

If you reach the maximum number of queries per minute (rate limit) in Content Library API, you will see a log message indicating that the system will retry your last request after a wait time.

This is an example of what the message looks like:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/398010007_1547315062763139_1392026401103332627_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=NP6X6VD0OGAAX_SFTrM&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCKU1SWTvndm9HaBhS17f_-tgq-DlUDoXfLdebijXhc5A&oe=65BEBA05)  
  

If you reach the maximum number of data records retrieved per seven-day rolling window (query budget), you will see an error message indicating that you have reached your allotted query budget and recommending that you retry your latest query later. In this case, the system does not handle retrying the request for you.

This is an example of what the message looks like:

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/397449533_1025873445329811_6969197869066569786_n.png?_nc_cat=107&ccb=1-7&_nc_sid=f537c7&_nc_ohc=WGs01JS5DaoAX99umgY&_nc_ht=scontent-cdg4-2.xx&oh=00_AfA-ykVKwerwXBPSK7bVPoxU_JiaLodSeBRU3qLLiqUcRA&oe=65BEE104)

Tips for staying below the limits
---------------------------------

In general, searching for common words and requesting to fetch all the results can exhaust your query budget. Consider narrowing your searches for more targeted results.

### Get your current usage

`get_query_budget()` is a method that displays your maximum number of data records retrieved per rolling 7-day period (query budget) and how much of that budget you have already used:

RPython

    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='1')
            
    client$get_query_budget()

    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    client.get_query_budget()

This is a sample of the output:

 
\[{'current\_usage': 101000,
  'preallocated\_rows\_for\_running\_queries': 0,
  'total\_usage': 101000,
  'max\_usage\_limit': 500000,
  'timestamp': 'Tuesday, July 18, 2023 06:03:05 PM PDT'}\]

* _current\_usage_ is the number of results already returned by completed queries in the current 7-day rolling time window as of the current timestamp.
    
* _preallocated\_rows\_for\_running\_queries_ is the number of results (rows) allocated for asynchronous queries that are in progress.
    
* _total\_usage_ is the sum of _current\_usage_ and _preallocated\_rows\_for\_running\_queries_.
    
* _max\_usage\_limit_ is the maximum number of queries allowed in a 7-day rolling window.
    
* _timestamp_ marks the point in time at which these statistics were collected.
    

#### Current usage for multimedia

If you are using the Meta Content Library API in an approved third-party cleanroom environment (as opposed to Meta's Researcher Platform), _and if that environment supports including multimedia in posts_, multimedia-specific query budget usage is also available as a `multimedia` JSON object with the following fields:

* _total\_usage_ is the number of calls with multimedia in the current 7-day rolling time window as of the current timestamp.
    
* _max\_usage\_limit_ is the maximum number of calls with media allowed in a 7-day rolling window.
    

The query budget specific to queries containing multimedia is 1000 queries per 7-day rolling window.

### Estimate response size for asynchronous queries

`get_estimate()` is a method that gives you a rough idea of how much data would be returned from a search you plan to run asynchronously. See [Estimating response size](https://developers.facebook.com/docs/content-library-api/guide-search-object#estimate) and [Asynchrounous search](https://developers.facebook.com/docs/content-library-api/guide-search-object#async-search) in the _Search Guide_ for more information on these topics.

**Points to keep in mind**:

* The API can only return up to 100,000 results from a single asynchronous search, so it can be helpful to know in advance if your search is likely to fail because the response size is too large.
    
* The query budget of 500,000 results in a rolling seven-day window can be used up quickly on just a few searches with high predicted results.
    

If the estimate comes out higher than 100,000, you might consider modifying the parameters to reduce the response size. You can continue to modify the search parameters and get new estimates until the search results are predicted to fall below the maximum allowed or close to the response size you prefer.

This is typically most useful for post searches because the number of results tend to be higher, but it can be used to estimate the number of results that would be returned by any search.

RPython

    # Request an estimate:
    post_search <- client$search_posts(q = 'dogs')
    estimate <- post_search$get_estimate()        
            
    # Display the estimate:        
    print(estimate)

    # Request an estimate:  
    post_search = client.search_posts(q='dogs')        
    estimate = post_search.get_estimate()
          
    # Display the estimate:        
    print(estimate)

Learn more
----------

* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/rate-limiting
Rate limiting and query budgeting
=================================

Meta Content Library and API both have limits at the individual researcher level that:

* Put a cap on the number of queries allowed per user per minute (a separate limit for each tool). This is called a _rate limit_.
    
* Put a cap on the number of retrieved data records (posts, for example) per user per seven-day rolling window. This limit, called a _query budget_, is shared between the two tools per user. In other words, a single researcher has a total query budget between the two tools, regardless if they are using just Content Library, just Content Library API, or both.
    

Maintaining a rate-limiting and query-budgeting policy ensures that the tools run efficiently and provide all users with consistent data access, unhindered by reduced performance. It also provides a measure of protection against system flooding.

What are the limits?
--------------------

### Rate limits for Content Library

* 60 queries over any one-minute interval

### Rate limits for Content Library API

* Synchronous search queries: 60 queries over any one-minute interval
    
* Asynchronous search queries: 1 query per minute
    

See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) for information about the difference between synchronous and asynchronous searches.

### Combined query budget per researcher

For Content Library and API combined, you can retrieve a maximum of 500,000 data records per seven-day rolling window. The rolling window is one week previous to the current timestamp (to the second). If you are blocked by hitting the query budget, you should not need to wait long before you try again.

If you are using the Content Library API in a third-party cleanroom environment, and if that environment supports including multimedia in posts, there is an additional query budget of 1000 queries with multimedia per rolling week.

How to request a limit increase
-------------------------------

If you have questions or concerns about the impact of your limits on your research, contact us through [Direct Support](https://developers.facebook.com/docs/content-library-and-api/direct-support).

Limit reached messaging
-----------------------

### Content Library

Content Library warns you when you get close to the maximum number of data records retrieved per seven-day rolling window (query budget) with a banner at the top of the page. This is an example of what the banner looks like:

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/367743972_262423759986978_211809594479650483_n.png?_nc_cat=102&ccb=1-7&_nc_sid=f537c7&_nc_ohc=jsN-z2cH3YYAX-3c11L&_nc_ht=scontent-cdg4-1.xx&oh=00_AfAh6CHmWAq6-6uoaRmc5rrYfsBX94-1-abvRnynIms66A&oe=65BF5964)

When you reach your query budget, you will see a different banner at the top of the page that looks like this:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/367729115_698453068806558_1327188573085519935_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=nKpmcd2YsUoAX9oe-fw&_nc_ht=scontent-cdg4-3.xx&oh=00_AfAdyEBW3zDyv1y9YRT-MMh5UWdSDEbKrZJXa0paGoF02A&oe=65BEBBA9)

The banner has a "Learn more" link, which will open the following message with additional details about rate limits:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/367733689_3623192734669772_7188247576546648393_n.png?_nc_cat=104&ccb=1-7&_nc_sid=f537c7&_nc_ohc=XOMdupwPXaAAX9j40ZS&_nc_ht=scontent-cdg4-3.xx&oh=00_AfA2Nj0WCJ6kluo-nZubUEDJgmOlLzAB6J8X9qX5RxCDFg&oe=65BE4BD5)

### Content Library API

If you reach the maximum number of queries per minute (rate limit) in Content Library API, you will see a log message indicating that the system will retry your last request after a wait time.

This is an example of what the message looks like:

![](https://scontent-cdg4-3.xx.fbcdn.net/v/t39.8562-6/398010007_1547315062763139_1392026401103332627_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=NP6X6VD0OGAAX_SFTrM&_nc_ht=scontent-cdg4-3.xx&oh=00_AfCKU1SWTvndm9HaBhS17f_-tgq-DlUDoXfLdebijXhc5A&oe=65BEBA05)  
  

If you reach the maximum number of data records retrieved per seven-day rolling window (query budget), you will see an error message indicating that you have reached your allotted query budget and recommending that you retry your latest query later. In this case, the system does not handle retrying the request for you.

This is an example of what the message looks like:

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/397449533_1025873445329811_6969197869066569786_n.png?_nc_cat=107&ccb=1-7&_nc_sid=f537c7&_nc_ohc=WGs01JS5DaoAX99umgY&_nc_ht=scontent-cdg4-2.xx&oh=00_AfA-ykVKwerwXBPSK7bVPoxU_JiaLodSeBRU3qLLiqUcRA&oe=65BEE104)

Tips for staying below the limits
---------------------------------

In general, searching for common words and requesting to fetch all the results can exhaust your query budget. Consider narrowing your searches for more targeted results.

### Get your current usage

`get_query_budget()` is a method that displays your maximum number of data records retrieved per rolling 7-day period (query budget) and how much of that budget you have already used:

RPython

    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='1')
            
    client$get_query_budget()

    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='2')
    
    client.get_query_budget()

This is a sample of the output:

 
\[{'current\_usage': 101000,
  'preallocated\_rows\_for\_running\_queries': 0,
  'total\_usage': 101000,
  'max\_usage\_limit': 500000,
  'timestamp': 'Tuesday, July 18, 2023 06:03:05 PM PDT'}\]

* _current\_usage_ is the number of results already returned by completed queries in the current 7-day rolling time window as of the current timestamp.
    
* _preallocated\_rows\_for\_running\_queries_ is the number of results (rows) allocated for asynchronous queries that are in progress.
    
* _total\_usage_ is the sum of _current\_usage_ and _preallocated\_rows\_for\_running\_queries_.
    
* _max\_usage\_limit_ is the maximum number of queries allowed in a 7-day rolling window.
    
* _timestamp_ marks the point in time at which these statistics were collected.
    

#### Current usage for multimedia

If you are using the Meta Content Library API in an approved third-party cleanroom environment (as opposed to Meta's Researcher Platform), _and if that environment supports including multimedia in posts_, multimedia-specific query budget usage is also available as a `multimedia` JSON object with the following fields:

* _total\_usage_ is the number of calls with multimedia in the current 7-day rolling time window as of the current timestamp.
    
* _max\_usage\_limit_ is the maximum number of calls with media allowed in a 7-day rolling window.
    

The query budget specific to queries containing multimedia is 1000 queries per 7-day rolling window.

### Estimate response size for asynchronous queries

`get_estimate()` is a method that gives you a rough idea of how much data would be returned from a search you plan to run asynchronously. See [Estimating response size](https://developers.facebook.com/docs/content-library-api/guide-search-object#estimate) and [Asynchrounous search](https://developers.facebook.com/docs/content-library-api/guide-search-object#async-search) in the _Search Guide_ for more information on these topics.

**Points to keep in mind**:

* The API can only return up to 100,000 results from a single asynchronous search, so it can be helpful to know in advance if your search is likely to fail because the response size is too large.
    
* The query budget of 500,000 results in a rolling seven-day window can be used up quickly on just a few searches with high predicted results.
    

If the estimate comes out higher than 100,000, you might consider modifying the parameters to reduce the response size. You can continue to modify the search parameters and get new estimates until the search results are predicted to fall below the maximum allowed or close to the response size you prefer.

This is typically most useful for post searches because the number of results tend to be higher, but it can be used to estimate the number of results that would be returned by any search.

RPython

    # Request an estimate:
    post_search <- client$search_posts(q = 'dogs')
    estimate <- post_search$get_estimate()        
            
    # Display the estimate:        
    print(estimate)

    # Request an estimate:  
    post_search = client.search_posts(q='dogs')        
    estimate = post_search.get_estimate()
          
    # Display the estimate:        
    print(estimate)

Learn more
----------

* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/data-deletion
Data deletion
=============

Researcher Platform JupyterHub environment programmatically deletes all Meta Content Library API research output data and generated local files from JupyterHub environments every 30 days. This ensures that updates made to the visibility of content on Facebook or Instagram are carried over to Researcher Platform in accordance with Meta data deletion policies.

The data deletion is carried out during a 24-hour maintenance window the first day of every month beginning at 12:00 AM PST and ending at 11:59 PM PST on the same day, during which you cannot log in to your JupyterHub environment.

What is and is not deleted
--------------------------

The following forms of data are deleted:

* All output cells in notebook files
* All non-notebook files on researchers' persistent storage
* All S3 bucket files including uploads carried out from within the JupyterHub environment, asynchronous query output, and all query results

The following forms of data are _not_ deleted:

* Notebook files (.ipyhb files)
* Notebook input cells (code and markdown)
* Graphics in notebook cells

The maintenance window
----------------------

The maintenance window, during which you will be unable to log into your JupyterHub environment, begins on the first day of every month at 12:00 AM PST. It lasts for 24 hours and ends at 11:59 PM PST on the same day.

When the maintenance window begins, this message is displayed in JupyterHub and remains until the window ends:

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/357539214_1310321563203938_4085783015753068939_n.png?_nc_cat=110&ccb=1-7&_nc_sid=f537c7&_nc_ohc=stff3SxQt00AX_ADLTY&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBy9VvF4VrCgyuroQq4ywuFK2G089dY8--OCzBJOuou2A&oe=65BF86A3)

Managing your data to avoid research disruption
-----------------------------------------------

To minimize the disruption to your research, consider taking the following measures:

* Since your input query cells are not affected by the data deletion, you can plan to rerun your queries and regenerate new outputs every 30 days. The output will not match exactly what you had previously because it will not include any user data that no longer meets visibility requirements for Content Library API.
    
* You can plan ahead to accommodate the maintenance window each month, so you are not caught by surprise, unable to work.
    
* You can plan to perform analysis on query results before a maintenance window occurs. Although the raw data is affected by the data deletion, your code, figures, tables, graphs and statistics from your analyses are not.
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/appendix
Appendix
========

The following reference materials are available to further enhance your use of the Meta Content Library and API in your work.

Documentation Contents
----------------------

|     |     |
| --- | --- |
| ### [Data dictionary](https://developers.facebook.com/docs/content-library-api/data)<br><br>Detailed information on the data fields available in the public content accessed by Meta Content Library and API. | ### [Field expansion](https://developers.facebook.com/docs/content-library-api/field-expansion)<br><br>Explains the concept of _field expansion_ which is available for some fields on certain nodes. |
| ### [Search quality](https://developers.facebook.com/docs/content-library-api/search-quality)<br><br>Review of the set of measures Meta uses for monitoring search quality and presentation of any known limitations to search functionality and performance. | ### [Get API code](https://developers.facebook.com/docs/content-library-api/get-api-code)<br><br>How to get an automatically generated code snippet for your Meta Content Library search that you can use in the Meta Content Library API. |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/data
Data dictionary
===============

This data dictionary describes the data names displayed in the Meta Content Library web UI (the Name column) if applicable, and the corresponding API fields returned in Meta Content Library API search responses (the API field column). In the API field column, some fields have nested fields indicated by a dot notation. These are referred to as _expanded fields_. See [Field expansion](https://developers.facebook.com/docs/content-library-api/field-expansion) for information about how to include some or all of a parent field's expanded fields in your queries.

Facebook Page
-------------

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Meta Content Library ID | id  | The Meta Content Library ID associated with the Facebook Page. | Content Library API |
| Name | name | The name of the Facebook Page. | Content Library<br><br>  <br><br>Content Library API |
| About | about | The short paragraph in the About section of the Facebook Page. | Content Library<br><br>  <br><br>Content Library API |
| Website | website | The external URL from the Facebook Page’s About section. | Content Library API |
| Description | description | The long paragraph in the About section of the Facebook Page. | Content Library<br><br>  <br><br>Content Library API |
| Verification status | verification\_status | The verification status of the Facebook Page. A Facebook Page with a verified badge indicates that Facebook has confirmed that it is the authentic presence for that person or brand. [Learn more.](https://www.facebook.com/help/196050490547892) | Content Library<br><br>  <br><br>Content Library API |
| Page categories | page\_categories | The list of up to three categories of the Facebook Page, selected by the Page manager. | Content Library<br><br>  <br><br>Content Library API |
| Location city | location.city | The self-reported, publicly accessible city location associated with the Facebook Page. | Content Library API |
| Location country | location.country | The self-reported, publicly accessible country location associated with the Facebook Page. | Content Library API |
| Location country code | location.country\_code | The self-reported, publicly accessible country code location associated with the Facebook Page. | Content Library API |
| Location name | location.name | The self-reported, publicly accessible location name associated with the Facebook Page. | Content Library API |
| Location region | location.region | The self-reported, publicly accessible region location associated with the Facebook Page. | Content Library API |
| Location zip | location.zip | The self-reported, publicly accessible location zip associated with the Facebook Page. | Content Library API |
| Location street | location.street | The self-reported, publicly accessible street location associated with the Facebook Page. | Content Library API |
| Location state | location.state | The self-reported, publicly accessible state location associated with the Facebook Page. | Content Library API |
| Page name change date | page\_transparency.page\_name\_changes.data.date | The date the Facebook Page’s name changed. | Content Library API |
| Page name old | page\_transparency.page\_name\_changes.data.old\_name | The old name of the Facebook Page prior to the name change. | Content Library API |
| Page name new | page\_transparency.page\_name\_changes.data.new\_name | The new name of the Facebook Page, following the name change. | Content Library API |
| Page merged date | page\_transparency.page\_merges.data.date | The date another Facebook Page merged with this Page. | Content Library API |
| Page merged | page\_transparency.page\_merges.data.page\_merged | The name of the Facebook Page that merged with this Page. | Content Library API |
| Creation date | creation\_date | The date the Facebook Page was created. | Content Library<br><br>  <br><br>Content Library API |
| Page manager countries | page\_transparency.admin\_countries.data.country | The predicted primary country locations of people who manage this Facebook Page. | Content Library<br><br>  <br><br>Content Library API |
| Count of Page managers by countries | page\_transparency.admin\_countries.data.count | The number of people who manage this Facebook Page predicted to be from the associated country. | Content Library<br><br>  <br><br>Content Library API |
| Page owner | page\_transparency.confirmed\_page\_owner | The confirmed owner associated with the Facebook Page. | Content Library API |
| Has active ads | page\_transparency.has\_active\_ads | Whether the Facebook Page has active ads or not. | Content Library API |
| Has run political ads | page\_transparency.has\_run\_political\_ads | Whether the Facebook Page has run political ads or not. | Content Library API |
| Followers | follower\_count | The number of followers of the Facebook Page. | Content Library<br><br>  <br><br>Content Library API |
| Page likes | like\_count | The number of likes of the Facebook Page. | Content Library API |

Facebook group
--------------

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Meta Content Library ID | id  | The Meta Content Library ID associated with the Facebook group. | Content Library API |
| Name | name | The name of the Facebook group. | Content Library<br><br>  <br><br>Content Library API |
| Description | description | The description of the Facebook group. | Content Library<br><br>  <br><br>Content Library API |
| Creation date | creation\_date | The date the Facebook group was created. | Content Library<br><br>  <br><br>Content Library API |
| Group original name | group\_transparency.original\_name | The original name of the Facebook group. | Content Library API |
| Group name change date | group\_transparency.name\_changes.data.date | The date the name of the Facebook group changed. | Content Library<br><br>  <br><br>Content Library API |
| Group name new | group\_transparency.name\_changes.data.new\_name | The new name of the Facebook group. | Content Library API |
| Group admin and moderator Page IDs | group\_transparency.admin\_and\_moderator\_page\_ids | The list of Meta Content Library IDs of Facebook Pages that are admins or moderators of the Facebook group. | Content Library API |
| Group owner type | group\_owners.data.type | The type of the group owner associated with the Facebook group.This field will display if the group owner is a professional profile or Page. Only the Meta Content Library Page ID will be shared. | Content Library API |
| Group owner ID | group\_owners.data.id | The Meta Content Library ID of the Facebook group owners.This field will display if the group owner is a professional profile or Page. Only the Meta Content Library Page ID will be shared. | Content Library API |
| Picture URL | picture\_url | The photo URL of the Facebook group. | Content Library API |
| Group members | member\_count | The number of members of the Facebook group. | Content Library<br><br>  <br><br>Content Library API |

Facebook event
--------------

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Meta Content Library ID | id  | The Meta Content Library ID associated with the Facebook event. | Content Library API |
| Name | name | The name of the Facebook event. | Content Library<br><br>  <br><br>Content Library API |
| Description | description | The description of the Facebook event. | Content Library<br><br>  <br><br>Content Library API |
| Creation time | creation\_time | The time the Facebook event was created. | Content Library API |
| Event start time | event\_start\_time | The start time of the Facebook event. Not available if the event is the parent of recurring event instances. [Learn more](https://developers.facebook.com/docs/content-library-api/guide-fb-events#recurring). | Content Library<br><br>  <br><br>Content Library API |
| Event end time | event\_end\_time | The end time of the Facebook event. Not available if the event is the parent of recurring event instances. [Learn more](https://developers.facebook.com/docs/content-library-api/guide-fb-events#recurring). | Content Library API |
| Going responses | going\_count | The number of Going responses on a Facebook event. Not available if the event is the parent of recurring event instances. [Learn more](https://developers.facebook.com/docs/content-library-api/guide-fb-events#recurring). | Content Library<br><br>  <br><br>Content Library API |
| Not going responses | not\_going\_count | The number of Not Going responses on a Facebook event. Not available if the event is the parent of recurring event instances. [Learn more](https://developers.facebook.com/docs/content-library-api/guide-fb-events#recurring). | Content Library API |
| Interested responses | interested\_count | The number of Interested responses on a Facebook event. Not available if the event is the parent of recurring event instances. [Learn more](https://developers.facebook.com/docs/content-library-api/guide-fb-events#recurring). | Content Library<br><br>  <br><br>Content Library API |
| Event type | event\_type | The type of Facebook event. Event types include single instance, recurring or instance of recurring. | Content Library API |
| Recurring event IDs | recurring\_event\_ids | The list of Meta Content Library IDs of the recurring instances of the Facebook event, if the event is recurring. Only available if the event is the parent of recurring event instances. [Learn more](https://developers.facebook.com/docs/content-library-api/guide-fb-events#recurring). | Content Library API |
| Parent event ID | parent\_event\_id | The Meta Content Library ID of the parent event of the Facebook event, if the event is recurring. Only available if the event is an instance of a recurring event. [Learn more](https://developers.facebook.com/docs/content-library-api/guide-fb-events#recurring). | Content Library API |
| Event owners type | event\_owners.data.type | The type of the event owner associated with the Facebook event. | Content Library API |
| Event owners ID | event\_owners.data.id | The Meta Content Library ID of the event owner associated with the Facebook event. This field will display if the event owner is a group, professional profile or Page. For events owned by professional profiles or Pages, only the Meta Content Library Page ID will be shared. | Content Library API |
| Place name | place.name | The self-reported, publicly accessible name of the place where the Facebook event is located. | Content Library API |
| Place location city | place.location.city | The self-reported, publicly accessible city where the Facebook event is located. | Content Library API |
| Place location country | place.location.country | The self-reported, publicly accessible country where the Facebook event is located. | Content Library API |
| Place location country code | place.location.country\_code | The self-reported, publicly accessible country code of the Facebook event’s location. | Content Library API |
| Place location name | place.location.name | The self-reported, publicly accessible name of the Facebook event’s location. | Content Library API |
| Place location region | place.location.region | The self-reported, publicly accessible region where the Facebook event is located. | Content Library API |
| Place location state | place.location.state | The self-reported, publicly accessible state where the Facebook event is located. | Content Library API |
| Place location street | place.location.street | The self-reported, publicly accessible street where the Facebook event is located. | Content Library API |
| Place location zip | place.location.zip | The self-reported, publicly accessible zip of the Facebook event’s location. | Content Library API |

Facebook post
-------------

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Meta Content Library ID | id  | The Meta Content Library ID associated with the Facebook post. | Content Library API |
| Text | text | The text of the Facebook post. Tags are excluded. | Content Library<br><br>  <br><br>Content Library API |
| Creation time | creation\_time | The time the Facebook post was created. | Content Library<br><br>  <br><br>Content Library API |
| Modified time | modified\_time | The time the Facebook post was most recently modified. | Content Library API |
| Language | lang | The content language of the Facebook post. Returns ISO 639-1 language code in 2-letter lowercase format. | Content Library (Filter only)<br><br>  <br><br>Content Library API |
| Likes | statistics.like\_count | The number of like reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Love reactions | statistics.love\_count | The number of love reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Wow reactions | statistics.wow\_count | The number of wow reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Haha reactions | statistics.haha\_count | The number of haha reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Sad reactions | statistics.sad\_count | The number of sad reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Angry reactions | statistics.angry\_count | The number of angry reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Comments | statistics.comment\_count | The number of comments on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Reactions | statistics.reaction\_count | The total number of reactions on the post. Reactions include: Like, Love, Care, Haha, Wow, Sad or Angry. | Content Library<br><br>  <br><br>Content Library API |
| Shares | statistics.share\_count | The number of times the post was shared. | Content Library<br><br>  <br><br>Content Library API |
| Care reactions | statistics.care\_count | The number of care reactions on the post. | Content Library<br><br>  <br><br>Content Library API |
| Views | statistics.views | The number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. For video posts, views are counted whether the video was played or not. Only posts with more than 100 views display the view count. A post displays no view count value if there were fewer than 100 views as of the last refresh. View counts for Facebook posts or reels made before January 1, 2017 are not available. View counts are not available for Facebook posts created in the last 5-7 days due to the refresh cycle. | Content Library<br><br>  <br><br>Content Library API |
| View counts last refreshed date | view\_date\_last\_refreshed | The date the view count was last refreshed. View counts are refreshed every 7 days for all Facebook posts. | Content Library<br><br>  <br><br>Content Library API |
| Post owner type | post\_owner.data.type | The type of post owner associated with the Facebook post. Post owner types include: Pages, groups and events. | Content Library<br><br>  <br><br>Content Library API |
| Post owner ID | post\_owner.data.id | The Meta Content Library ID of the owner associated with the Facebook post. | Content Library API |
| Post owner name | post\_owner.data.name | The name of the post owner associated with the Facebook post. | Content Library<br><br>  <br><br>Content Library API |
| Media type | media\_type | The media type included in the Facebook Post. Media types include photos, videos and reels, and miscellaneous (including links, reshares, and text-only posts). | Content Library |
| Branded content Page ID | branded\_content\_page\_id | The Meta Content Library ID of the Page associated with the Facebook post. Included if the post has branded content. [Learn more.](https://www.facebook.com/business/help/788160621327601?id=1912903575666924) | Content Library API |
| Link attachment fields description | link\_attachment\_fields.description | The description of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields link | link\_attachment\_fields.link | The URL of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields name | link\_attachment\_fields.name | The name of the link attachment included in the Facebook post. | Content Library API |
| Link attachment fields caption | link\_attachment\_fields.caption | The caption of the link attachment included in the Facebook post. | Content Library API |
| Shared post ID | shared\_post\_id | The Meta Content Library ID of the reshared post included in the Facebook post. | Content Library API |

Facebook post third-party cleanroom only
----------------------------------------

The following data dictionary entries are only available when using the Content Library API in an approved third-party cleanroom that supports the specific functionality.

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Multimedia type | multimedia.type | The type (photo or video) of the multimedia content. | Content Library API |
| Multimedia ID | multimedia.id | Anonymized ID of the photo or video content. | Content Library API |
| Multimedia URL | multimedia.url | URL within a storage location to which the multimedia content has been downloaded by the third-party cleanroom if the cleanroom system is unable to provide the multimedia directly in the search results. | Content Library API |

Instagram account
-----------------

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Meta Content Library ID | id  | The Meta Content Library ID associated with the Instagram account. | Content Library API |
| Account type | account\_type | The type of public Instagram account. Creator, business, and personal accounts are valid types.<br><br>Public Instagram accounts include professional accounts for businesses and creators. They also include a subset of personal accounts that have privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT2eaRNscgisi8R0c-d2h0w8VHWuzi15kYsBVixlOkUTM9a773Jozwknk8iLxD9fUp4h9r6qXD_7Vtau-65bETl2-ZZF61l-bTvrQpzMbr5FJQAUZ3_CZAgCxOnOFYiO6OPX3Ji31Ba2eet_) and have either a verified badge or 50,000 or more followers. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT0-r6ZnK90zwC-O7rmvuWB5PJMLpn_w5E43-1_1zyXFUyHREQHjbQ8ecZK_DoWZQyPr-r9N1k0Gumi4OF-jMRCH3Jn3taFTKmNf9H5kvlberDNy8HI2oIKva6MIP6pCVUicCnW0gfXj3-Ss) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. | Content Library API |
| Is verified | is\_verified | Whether the Instagram account has a verified badge. A verified badge in this context refers to accounts confirmed as authentic and not to those with a paid Meta Verified subscription. [Learn more.](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F854227311295302&h=AT1krWf12XlconGGQonMJslfgjneKdRolS6emu9PNMDUMD7pRmfRR_bcLUpUr3GUI7ln_pBk5oAm5Hiv07jCGsTZOsYeTZK3J_ck2HFuCqzyB-5fefsYfxBR4aYVzQ9sxqoyaoswnmE5UMUz) | Content Library<br><br>  <br><br>Content Library API |
| Followers | follower\_count | The number of followers of the Instagram account. | Content Library<br><br>  <br><br>Content Library API |
| Following | following\_count | The number of accounts the Instagram account is following. | Content Library API |
| Website | website | The external website URL of the Instagram account. | Content Library API |
| Name | name | The name of the Instagram account. | Content Library<br><br>  <br><br>Content Library API |
| Biography | biography | The description of the Instagram account. | Content Library<br><br>  <br><br>Content Library API |
| Creation date | creation\_date | The date the Instagram account was created. | Content Library API |

Instagram post
--------------

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Meta Content Library ID | id  | The Meta Content Library ID associated with the Instagram post. | Content Library API |
| Text | text | The text of the Instagram post. Tags are excluded. | Content Library<br><br>  <br><br>Content Library API |
| Creation time | creation\_time | The time the Instagram post was created. | Content Library<br><br>  <br><br>Content Library API |
| Modified time | modified\_time | The time the Instagram post was most recently modified. | Content Library API |
| Language | lang | The content language of the Instagram post. Returns ISO 639-1 language code in 2-letter lowercase format. | Content Library API |
| Comments | statistics.comment\_count | The number of comments on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Likes | statistics.like\_count | The number of like reactions on the post or reel. | Content Library<br><br>  <br><br>Content Library API |
| Views | statistics.views | The number of times the post or reel was on screen, not including times it appeared on the post owner’s screen. For video posts, views are counted whether the video was played or not. Only posts with more than 100 views display the view count. A post displays no view count value if there were fewer than 100 views as of the last refresh. View counts for Instagram posts or reels made before October 1, 2022 are not available. View counts are not available for Instagram posts created in the last 3-5 days due to the refresh cycle. | Content Library<br><br>  <br><br>Content Library API |
| View counts last refreshed date | view\_date\_last\_refreshed | The date the view count was last refreshed. View counts are refreshed every 3 days for all Instagram posts and reels. | Content Library<br><br>  <br><br>Content Library API |
| Post owner account type | post\_owner.type | The account type of the post owner associated with the Instagram post. Post owner types include business, creator, and personal. For personal accounts, only those with privacy [set to public](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F517073653436611&h=AT0RgShRVvlHXcEl2J9_VJ7rsUDXaqFBtFsc2IsJGhO7TnG1VYjEURs_l-Xwi5co1LDJkTIY4VS_NKpIGeW9OJE56wEH5uD0Fn2aPYNRoTReTsyMYUCYEtbARdY8jktrS8lYlyRREGtqlIEo) and with either a verified badge or 50,000 or more followers are included. A [verified badge](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F733907830039577%3Fhelpref%3Dfaq_content&h=AT3l6a8eoqRxtcQBUbFK85rjLZk0jbJFtuz0q7_icHHXKzgkHiXCiW6yJL_p6Nxf38resgDJJzWJA_pNSzpNyoir4M_rbssr-hyj9p_b8Q13Gcnntskrp5PuNl1ACcMtMIQvzpOAnLfy6TnX) in this context refers to accounts confirmed as authentic and not those with a paid Meta Verified subscription. | Content Library API |
| Post owner ID | post\_owner.id | The Meta Content Library ID of the owner associated with the Instagram post. | Content Library API |
| Is branded content | is\_branded\_content | Whether the Instagram post has branded content or not. [Learn more.](https://l.facebook.com/l.php?u=https%3A%2F%2Fhelp.instagram.com%2F1123581461537025%2F&h=AT3ZdyvyC8cShDadIO7KI432Xs5hqirOW4UeI9nYmSefhdUB17Cp6XVG9evr6z_pvWyBVbScqSrDjfutOXNDm31CqZkeW0a_7cDTs9tBVFtBDptk8DDWYtraKX_Dy_nJKgMmCyJT63Igkoxv) | Content Library API |
| Media type | media\_type | The media type included in the Instagram post. Media types include albums, photos, and videos and reels. | Content Library<br><br>  <br><br>Content Library API |
| Hashtags | hashtags | The list of hashtags included in the Instagram post. | Content Library<br><br>  <br><br>Content Library API |

Instagram post third-party cleanroom only
-----------------------------------------

The following data dictionary entries are only available when using the Content Library API in an approved third-party cleanroom that supports the specific functionality.

| Name | API field | Description | Products |
| --- | --- | --- | --- |
| Multimedia type | multimedia.type | The type (photo or video) of the multimedia content. | Content Library API |
| Multimedia ID | multimedia.id | Meta Content Library ID associated with the photo or video content. | Content Library API |
| Multimedia URL | multimedia.url | URL within a storage location to which the multimedia content has been downloaded by the third-party cleanroom if the cleanroom system is unable to provide the multimedia directly in the search results. | Content Library API |

Learn more
----------

* [Field expansion](https://developers.facebook.com/docs/content-library-api/field-expansion)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/field-expansion
Field expansion
===============

There are a number of fields in the data available through the Meta Content Library API that are nested. For example, the `statistics` field contains the `like_count`, `haha_count`, and several other fields. When you create search objects, you might want to include some or all of the nested fields in your search. _Field expansion_ allows you to perform queries for multiple fields and their nested fields in a single call. We refer to the nested fields as _expanded fields_.

In the [Data dictionary](https://developers.facebook.com/docs/content-library-api/data), expanded fields are indicated by a dot notation. For example, `statistics.like_count` indicates that `like_count` is available within `statistics`. To specify expanded fields in your search objects, you can either use this dot notation or you can append the names of the expanded fields in curly braces after the parent field. See the examples in this section.

Specifying multiple fields
--------------------------

You can specify which multiple fields you want returned on any associated data by using the `fields` parameter, with the field names separated by commas.

RPython

    library(contentlibraryapi)
    client <- ContentLibraryAPIClient$new(version='1')
            
    post_search <- client$search_posts(q='cybercrime', fields="id,text")
    post_search$query_next_page()

    from contentlibraryapi import ContentLibraryAPIClient
    client = ContentLibraryAPIClient.get_instance(version='1')
    
    
    post_search = client.search_posts(q="cybercrime", fields="id,text")
    display(post_search.query_next_page())

Specifying expanded fields
--------------------------

You can specify which expanded fields you want returned on any associated data by using the dot notation in your query to specify first the parent field, then the expanded field (such as `statistics.haha_count`).

RPython

    post_search <- client$search_posts(q='cybercrime', fields="id,statistics.like_count,statistics.haha_count")
    post_search$query_next_page()

    post_search = client.search_posts(q="cybercrime", fields="id,statistics.like_count,statistics.haha_count")
    display(post_search.query_next_page())

Alternatively, you can append a comma-separated list of expanded field names wrapped in curly braces to the end of any parent field name.

RPython

    post_search <- client$search_posts(q='cybercrime', fields="id,statistics{like_count,haha_count}")
    post_search$query_next_page()

    post_search = client.search_posts(q="cybercrime", fields="id,statistics{like_count,haha_count}")
    display(post_search.query_next_page())

If you specify a field but do not specify any of its expanded fields, default expanded fields on the associated node are included in the response. If you omit the `fields` parameter altogether, default expanded fields on default parent fields on the associated data are included in the response.

Learn more
----------

* [Data dictionary](https://developers.facebook.com/docs/content-library-api/data)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/search-quality
Search quality approach
=======================

This document describes Meta's approach to search quality for Meta Content Library and API.

Definitions
-----------

* **Entities** Objects in the social graph returned by Meta Content Library and Meta Content Library API which generate or contain content and are associated with a unique ID in internal systems. Includes Facebook Pages, groups, events and posts, as well as Instagram accounts and posts.
    
* **Content** Text and other data associated with entities, returned as fields in Meta Content Library and API.
    
* **Eligible / Visible** Entities or content permitted to be returned in Meta Content Library and API which meet privacy commitments and legal requirements. See [Frequently asked questions](https://developers.facebook.com/docs/content-library-api/disclosures) for details.
    
* **Endpoint** Meta Content Library or API endpoint corresponding to a specific type of entity.
    

Search overview
---------------

Queries in Meta Content Library and API are powered by a version of Facebook’s [search engine infrastructure](https://research.facebook.com/publications/unicorn-a-system-for-searching-the-social-graph/), which relies on a combination of indexing and ranking to return relevant entities. The retrieval function combines matched and ranked IDs from a query using the same distributed [memory caching layer](https://l.facebook.com/l.php?u=https%3A%2F%2Fengineering.fb.com%2F2013%2F06%2F25%2Fcore-data%2Ftao-the-power-of-the-graph%2F&h=AT1-Q7Wgi5KB4QxoLpmG2GlumDaDJaFx-Gy4AGLKCweWro_nv71laUM-gb4OHWV8kv9t0ThHlPx8T-qY162Or5GqbNhyBSRrjmGQu5qDDKIFEGD_cc-uyOs2xAeRrRTyZi5Yy2wUs4CqPANp) which serves live platform content. This ensures that results represent the most current state of content on the platform and meet privacy-preserving visibility criteria (see [Frequently asked questions](https://developers.facebook.com/docs/content-library-api/disclosures) for details).

As content is created or modified on Meta platforms, associated entities are registered to a search index built from individual words extracted from text fields as _tokens_. Tokenization generally isolates words separated by spaces or punctuation ( ?@$%^\*()+=~\[{}\];:"<>|. ), with some URL normalization and locale-specific adjustments for non-English languages. Tokenization is exact, in that it does not introduce additional word variants ("cats" will not be tokenized to "cat"). Direct mentions of users or other platform entities (via @) are not tokenized and are scrubbed from returned text fields, and are thus not searchable.

At query time, relevant content is identified by exact matching between tokens and individual search terms. Candidate matches are then subject to additional filtering via Boolean query logic (see [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)) and other selected filters. Matching is performed independently by word in a query, meaning that searching by phrase is not supported (queries “All for one” and “One for all” are equivalent).

Initial testing
---------------

We expect our methodology to measure search quality to evolve over time. Here we outline a set of initial tests of search quality in the Meta Content Library and API. The systems which underlie search are complex and the data models as well as privacy rules which determine content visibility evolve over time, meaning that quality regressions can occur. Furthermore, as we develop the product, we welcome feedback about bugs or unexpected behavior from the user community. See [Appendix](#appendix) on this page for details on reporting issues.

### Methods

#### Initial test queries

We generated test search results for each endpoint (Facebook Pages, groups, events, and posts, and Instagram business and creator accounts, and posts) using a sample of 130 terms chosen to span a breadth of set size (for example, obscure words such as _stopthesteal_ and common words such as _spray_), polarization (for example, neutral words such as _sugar_ and socially charged words such as _transphobic_), as well as most queried keywords by researchers in Meta platforms. These initial test queries consisted of single terms all in English without non-Latin characters or any symbols (for example ‘, #, $ or @). Additional query parameters for each endpoint are listed in [Test search scope for endpoints](#scope). Test queries resulting in > 100,000 results were excluded from further analysis.

#### Validation data

Lists of expected entities for test queries were generated from regex-based full-text searches on a SQL-like database backend. Tables in this database are built from periodic snapshots of logged platform content and thus are known to differ slightly from what is available in Meta Content Library and API at search time due to time lags and incomplete visibility filters. This dataset thus constitutes a secondary validation channel rather than source of truth and regressions in quality metrics may be a composite of both true indexing errors and/or measurement noise. See [Caveats and known limitations](#caveats).

### Recall

In principle, entities should be returned when (a) there is an exact match with search term(s), (b) the content is eligible to be retrieved, and (c) the total corpus of matching results does not exceed the technical query limit of 100,000 results.

We measured recall as follows:

(entities returned) ∩ (entities expected) / (entities expected)

The following table shows the average of daily recall values across test queries from November 8th, 2023 to November 15th, 2023.

| Endpoint | 20th percentile recall | Median |
| --- | --- | --- |
| Facebook Page | 96% | 98% |
| Facebook group | 93% | 96% |
| Facebook event | 90% | 93% |
| Facebook post | 85% | 92% |
| Instagram account | 98% | 99% |
| Instagram post | 90% | 94% |

### Rank recall

Results which represent the _top N_ results ordered by creation time or views should also be complete. For Meta Content Library, which returns a truncated list of ranked results, we generated a _ranked_ version of recall which is calculated as follows:

(top N entities) ∩ (top N expected entities) / (top N expected entities)

The following table shows the average of daily recall values for the top 1000 results ranked by creation time and view across test queries from November 8th, 2023 to November 15th, 2023.

| Endpoint | 20th percentile ranked recall | Median ranked recall |
| --- | --- | --- |
| Facebook post (ranked by creation time) | 86% | 92% |
| Instagram post (ranked by creation time) | 64% | 75% |
| Facebook post (ranked by view) | 52% | 63% |
| Instagram post (ranked by view) | 62% | 73% |

### Precision

Only results which exactly match search terms should be returned, excluding, for instance, partial index matches (broom → broomstick) or fuzzy matches (broom → mop). Precision was measured as:

(returned entities matching query exactly) / (all returned entities)

The following table shows the range in average daily precision values across test queries by endpoint from November 8th, 2023 to November 15th, 2023.

| Endpoint | 20th percentile precision | Median precision |
| --- | --- | --- |
| Facebook Page | 99% | 99% |
| Facebook group | 99% | 99% |
| Facebook event | 99% | 99% |
| Facebook post | 99% | 99% |
| Instagram account | 97% | 98% |
| Instagram post | 98% | 99% |

### Representativeness

In cases where incomplete results are returned (recall < 100%), results may be useful provided they are not overly biased (that is, they are consistent with a random uniform sample of the complete results). We measured representativeness using a series of statistical tests for bias at the individual query level.

#### Query-level bias

For each test query we compared whether a summary statistic (mean, for example) calculated using the results from the Meta Content Library API reasonably approximated results obtained from the validation dataset (which has high recall). Across several data dimensions including engagement, exposure, and creator demographics, we performed a series of t-tests comparing means derived from the Meta Content Library API to means derived from the validation dataset. We then calculated the percent of queries which lacked statistically significant evidence of bias (p > 0.05). Finally, we calculated the mean of metrics across all dimensions.

We performed two versions of this test using methods which differed in their level of sensitivity to small differences between Meta Content Library API results and validation data. In the first version, we used a Welch’s T-test, which is appropriate for detecting major distributional differences between datasets that might affect inference about population-level traits. It is less sensitive to small differences between datasets and we expect most appropriate for research use cases involving trends and summaries.

The following table shows average daily percent of test queries generating non-biased results using a Welch’s T-test across endpoints from November 8th, 2023 to November 15th, 2023.

| Endpoint | Representativeness - Welch t-test |
| --- | --- |
| Facebook Page | 96% |
| Facebook group | 86% |
| Facebook event | 78% |
| Facebook post | 86% |
| Instagram account | 97% |
| Instagram post | 96% |

In the second version of the query-level bias test we compared Meta Content Library API and validation datasets using a pairwise t-test (incorporating covariance between samples). This test is more powered to detect differences between datasets and appropriate for assessing whether small subsets of entities may be missing or over-represented. For instance, this metric could highlight significant bias even with 98% recall and a negligible difference in means, due to any imbalance in the remaining data. Given known issues with the validation dataset failing to exclude some ineligible entities based on visibility criteria, we expect these measures to be more conservative and likely underestimates of representativeness.

The following table shows percent of test queries generating non-biased results using a paired t-test across endpoints from November 8th, 2023 to November 15th, 2023.

| Endpoint | Representativeness - paired t-test |
| --- | --- |
| Facebook Page | 80% |
| Facebook group | 54% |
| Facebook event | 41% |
| Facebook post | 53% |
| Instagram account | 74% |
| Instagram post | 64% |

Search quality measurement expansion
------------------------------------

While in initial testing we focused on English to measure the search quality, in our expansion, we extended the exact same methodology to other languages and advanced search (search with logic operators AND, OR and NOT).

### Other languages

We used the same methodology to measure the search quality of the queries in Arabic, German and Hindi. These languages were selected based on the language features that the team believe are most likely to impact search quality. The features that the team considered are diacritics (such as accents), non-Roman characters, and right-to-left. We also wanted to cover at least one non-English European language.

Based on the analysis, we learned:

* The overall search quality of all the new languages is about the same level as English single keywords.
    
* The precision is over 95% for all endpoints in new languages.
    
* Since the search quality is reasonable for these languages, we expect to see very similar results for most other languages too.
    

The following table shows all metric values across test queries by language and endpoint from November 8th, 2023 to November 15th, 2023. Representativeness is an average across all dimensions that are mentioned in the representativeness section.

| Language | Endpoint | Recall | Precision | Representativeness - paired t-test | Representativeness - Welch t-test |
| --- | --- | --- | --- | --- | --- |
| Arabic | Facebook Page | 96% | 99% | 93% | 99% |
| Arabic | Facebook group | 92% | 99% | 41% | 61% |
| Arabic | Facebook event | 82% | 99% | 80% | 97% |
| Arabic | Facebook post | 91  | 99% | 70% | 94% |
| Arabic | Instagram account | 93% | 99% | 87% | 91% |
| Arabic | Instagram post | 80% | 99% | 85% | 97% |
| German | Facebook Page | 97% | 99% | 96% | 99% |
| German | Facebook group | 95% | 99% | 76% | 95% |
| German | Facebook event | 95% | 99% | 67% | 94% |
| German | Facebook post | 88  | 99% | 73% | 96% |
| German | Instagram account | 99% | 99% | 95% | 99% |
| German | Instagram post | 91% | 98% | 88% | 99% |
| Hindi | Facebook Page | 96% | 99% | 93% | 99% |
| Hindi | Facebook group | 96% | 99% | 39% | 61% |
| Hindi | Facebook event | 87% | 99% | 77% | 96% |
| Hindi | Facebook post | 92  | 99% | 71% | 95% |
| Hindi | Instagram account | 97% | 99% | 94% | 100% |
| Hindi | Instagram post | 73% | 99% | 80% | 96% |

We are also aware of a few limitations that our system has for other languages. The limitations are as follows:

* Meta Content Library API does not read any keywords with “ß” in German or semi-space (half-space) in Arabic.
    
* In Arabic, a word can be written with and without diacritics. Content Library API can only find the exact match for each form. Thus, if a researcher wants to find all posts related to that keyword, they have to search all forms of those keywords to get full results. For example, if a researcher need to find all post related to term مهاجر, they need to search مُهاجِر or مُهاجر or مهاجِر or مهاجر to get all the results.
    

### Advanced search

Advanced search includes searching keyword combinations with logic operators AND, OR and NOT. The following table shows all metric values across advanced search test queries by endpoint from November 8th, 2023 to November 15th, 2023. Representativeness is an average across all dimensions that are mentioned in the representativeness section.

| Entity type | Recall | Representativeness - Paired t-test | Representativeness - Welch t-test |
| --- | --- | --- | --- |
| Facebook Page | 95% | 77% | 94% |
| Facebook group | 93% | 71% | 93% |
| Facebook event | 90% | 59% | 83% |
| Facebook post | 83% | 70% | 93% |
| Instagram account | 98% | 79% | 99% |
| Instagram post | 78% | 83% | 99% |

Caveats and known limitations
-----------------------------

#### Why would results be inconsistent from one time point to another?

Inconsistencies between identical searches made at separate time points can be caused by entity visibility changes over time, which may be due to content being created, deleted or modified. There may also occasionally be short lags between when content is created or modified and when it is indexed.

#### Why am I not seeing an entity I can find on the platform?

Apart from coverage gaps or delivery issues mentioned below (see [Factors affecting recall](#recallfactors)), it is possible the content is not eligible to be visible in the Meta Content Library and API. The visibility rules for content are complex and constantly evolving with new policies and regulations, making it possible that some content could be theoretically viewed by an individual on platform but not exposed via the Meta Content Library and API. For instance, visibility of some content is geographically restricted to users from the country where the content was produced. Also, direct mentions (via @) are not searchable, meaning that a result will not be returned if a matching term is only found in a direct mention.

#### Why would a search result not match my query?

Apart from tokenization issues listed below (see [Factors affecting precision](#precisionfactors)), it is possible that the content actually does contain the search terms, but they are found in different text fields or far apart within the text. Search matches query terms independently and scans all text fields visible from the UI. It also does not support phrase searching. Thus a search for “Walter Payton” could match a page listing basketball players “Walter Williams” and “Gary Payton” without reference to a “Walter Payton” anywhere in the text.

### Factors affecting recall

* False positives in the validation data (denominator of recall equation). In our tests, we have found that the validation dataset may occasionally include non-eligible entities for a given search term due to lags between real-time content visibility and privacy status and their representation in the databases used for validation (see validation data presented earlier). This means that true recall estimates are likely underestimated.
    
* Edge cases or gaps in coverage (true negatives). Indexing data at the scale which Meta operates means that occasionally some content may be imperfectly indexed or missed. Furthermore, internal data models may change, such as when new features for creating and sharing content on platform are added. Thus there may be a lag between when content is available on platform and when it is indexed. As we improve and scale the product, we appreciate any reported cases of missing data from search (see [Appendix](#appendix) on this page for details).
    
* Asynchronous delivery issues. The Meta Content Library and API’s entity loading mechanisms are complex and memory-intensive at scale. Occasionally, the loading process for an entity can become too memory-intensive and fail, resulting in the exclusion of that entity from the returned results.
    

### Factors affecting precision

* String-matching used to validate precision is unable to approximate tokenization rules. Precision is checked using basic regular expression searches with strict definitions of word boundaries. However tokenization may be more flexible, especially with different language localizations, text involving unicode, URLs, and other patterns. The existence of these edge cases means that precision will be under-estimated to some extent.
    
* The search term was tokenized in a context-specific way. Occasionally words with unicode symbols, non-English characters, accent marks or URLs may be tokenized in a form that differs from its presented value. For instance, the content with the French word `congrégation` may be returned for a query on the English word `congregation`, despite the literal difference between the acute accented e and its English counterpart.
    
* The index has matched text not returned by the Meta Content Library or API. In some cases, content with complex, nested data models such as reshares may contain text fields that are tokenized and indexed but not returned by the Meta Content Library or API. We appreciate user feedback identifying such cases (see [Appendix](#appendix) on this page for details).
    
* For the Facebook posts endpoint, there is a known issue involving post reshare text being indexed but not returned in the Meta Content Library API. These posts may either have no visible text (since they are reshares), or the text returned may not contain any mention of the query term. We are exploring this issue further.
    

### Factors affecting representativeness

* Representativeness issues generally stem from the same factors affecting recall. In these cases there is a population of entities which are either (a) not returned by the Meta Content Library API due to gaps in indexing / delivery, or (b) incorrectly included in the validation dataset adding noise to the calculation. If these groups of entities have similar properties along the data dimensions tested they can influence the representativeness metrics
    
* The per-query bias test uses a probabilistic statistical test which uses an alpha = 0.05 cutoff by convention. Thus for each test term there is a 5% probability that the test will be a false positive (Type I error rate).
    

Appendix
--------

### Disclosures

Data governance and sources described in this document may change from time to time and the metrics presented here may not be representative of current operations at Meta. Due to issues such as erroneously logging the data sources from which these metrics are created, these metrics may suffer from fluctuating data quality and incompleteness, which may lead to fluctuating accuracy. We disclose known fluctuations where possible.

Researchers using this data are responsible for conducting standard and thorough data cleaning processes, and are responsible for ensuring that their analyses are accurate. It is expected that researchers may find issues with the data when conducting their analysis. We encourage researchers to share any findings with us. This may include, but is not necessarily limited to, data quality, validity, or fidelity issues. Given the historical nature of the data and lapsed retention periods, we may not be able to fix the issues identified, but in such cases we will work to disclose them. Please reach out to us through [Direct Support](https://developers.facebook.com/docs/content-library-and-api/direct-support).

### Disclaimers

Meta works diligently and utilizes a variety of quality assurance measures to improve the accuracy, quality, and reliability of the data it shares for research purposes. However, given the volume of data released and the imperfection of any quality assurance process, inaccuracies persist. Meta makes no representation or warranty, express or implied, including without limitation, any warranties of fitness for a particular purpose or warranties as to the quality, accuracy or completeness of data or information. By accessing this data, researchers acknowledge that the data may contain some nonconformities, defects, or errors. Meta does not warrant that the data will meet the researcher's needs or expectations, that the use of the data will be uninterrupted, or that all nonconformities, defects, or errors can or will be corrected.

### Test search scope for endpoints

The following table summarizes the test search scope for all endpoints

| Endpoint | Test search scope |
| --- | --- |
| Facebook Page | Eligible Facebook pages created within the year prior to the query date |
| Facebook group | All eligible Facebook groups |
| Facebook event | Eligible Facebook events created within the year prior to the query date |
| Facebook post | Eligible posts created within two days prior to the given query date |
| Instagram account | Eligible Instagram Creator and Business accounts created within a year prior to the query date |
| Instagram post | Eligible posts created within a day prior to the given query date |

Learn more
----------

* [Facebook's search engine infrastructure](https://research.facebook.com/publications/unicorn-a-system-for-searching-the-social-graph/)
    
* [Distributed memory caching layer](https://l.facebook.com/l.php?u=https%3A%2F%2Fengineering.fb.com%2F2013%2F06%2F25%2Fcore-data%2Ftao-the-power-of-the-graph%2F&h=AT2ZqqJyY6US4VZIFjvniRAGkuLUPEmoiHtL_q2x49-2haTJsUSADgwPxNj_sVpqgnAk1boA21BeFx59cF3BKp1PaqKeA2TsE7oP-iwbRzZxmr2ds1zp3SN-GHO3cS7Z1JAZzJIP8Gbpiq_y)
    
* [Advanced search guidelines](https://developers.facebook.com/docs/content-library-api/adv-search)
    
* [Frequently asked questions](https://developers.facebook.com/docs/content-library/disclosures)
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/get-api-code
Get API Code
============

Get API Code is a tool within Meta Content Library that automatically generates a Python or R code snippet corresponding to your current search that you can copy and paste into your Meta Content Library API Jupyter notebook.

**Remember the limits**

If you submit a synchronous query in the Content Library API that would return more than 1000 results, you will only see the top 1000.

If you submit an asynchronous query in the API that would return more than 100,000 results, the API will give you an error message and will not complete the query.

The automatically generated R or Python code might return more than 100,000 results. Be sure to check the very top of the Content Library search results to see the size of the results before you use the same search in the API.

In Content Library
------------------

### Define your search

Select the parameters for your search. The [**About**](https://www.facebook.com/transparency-tools/content-library/dataset/1119037145491882/about/) page in the web UI describes all the filters that are available.

### Open the Get API Code tool

Click **</>** in the top menu bar (mouse over the button to see the label).

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/397217799_6715388071870174_6446816218835772110_n.png?_nc_cat=109&ccb=1-7&_nc_sid=f537c7&_nc_ohc=Iv74FI63udAAX_04d0F&_nc_ht=scontent-cdg4-2.xx&oh=00_AfBry9IlL0zXCN41KbqhYNlTbJYeKx2c-7B2Tc_RYg-vRg&oe=65BE64FC)  
  

### Select Python or R

A new window opens in which your search parameters are listed, and the automatically-generated Python and R code that corresponds to your current search parameters is displayed in a tabbed code block. Click the tab corresponding to your language selection.

![](https://scontent-cdg4-2.xx.fbcdn.net/v/t39.8562-6/362617090_680365873510245_5275517031591126227_n.png?_nc_cat=109&ccb=1-7&_nc_sid=f537c7&_nc_ohc=n5XEes0r9JQAX-PJsbS&_nc_ht=scontent-cdg4-2.xx&oh=00_AfD9XUM9CWw2ywbnkk0Sr23yQH6BEBnDmtHWDglDarVjkA&oe=65BFCE87)

### Copy the code snippet

With the correct tab selected, click **Copy to Clipboard** below the code block.

The code block also includes instructions for submitting the code to the API as an asynchronous search which processes in the background. See [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object) to learn about the difference between synchronous (default) and asynchronous searches.

### Go to Content Library API

At the bottom of the **Get API Code** window, there is a **Go to Content Library API** button that opens the Content Library API sign-in window.

VPN connection is required for Content Library API:

* The **Go to Content Library API** button is clickable if you are connected to VPN.
    
* If you believe you are connected, but the button is not clickable, try refreshing your browser.
    
* For Content Library API getting started information including VPN access, see [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start).
    

In Content Library API
----------------------

### Paste the snippet into a notebook cell

Paste the code representing your search (query) into a blank cell in your Jupyter notebook. Be sure the language (R or Python) of the notebook matches the language of the code you copied. If you have not already set up your Jupyter environment, see [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start) for guidance.

![](https://scontent-cdg4-1.xx.fbcdn.net/v/t39.8562-6/278392598_315887847317792_4897557074894235014_n.png?_nc_cat=105&ccb=1-7&_nc_sid=f537c7&_nc_ohc=IWgWj5JbcNMAX9ybYB0&_nc_ht=scontent-cdg4-1.xx&oh=00_AfBdyZRLWw19weTAz07hYpqwf4BwAsLQkHYFmtCXLIxizw&oe=65BFA583)

### Run the code

Click the triangular button to run the code and display the results.

Learn more
----------

* [Content Library API documentation](https://developers.facebook.com/docs/content-library-api)
* [Search guide](https://developers.facebook.com/docs/content-library-api/guide-search-object)
* [Getting started](https://developers.facebook.com/docs/content-library-api/quick-start)

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/get-help
Get Help
========

For support questions related to Meta Content Library and API, we use a tool called **Direct Support** to quickly triage your questions, routing each one to the most appropriate expert. To get set up with Direct Support and for instructions on using it effectively, see [Direct Support](https://developers.facebook.com/docs/content-library-and-api/direct-support).

**But first**:

* For answers to many common questions, see [Frequently asked questions.](https://developers.facebook.com/docs/content-library-api/disclosures)  
      
    
* For questions related to the application for access and eligibility requirements, please refer to the Meta Content Library and API [application page](https://l.facebook.com/l.php?u=https%3A%2F%2Fsomar.infoready4.com%2F%23freeformCompetitionDetail%2F1910793&h=AT2JVm8YKnz5E9x9rUOAqXDwSpEdTyZbtM4zrYXmCJ_wq4k7NI9njI_zJaiHwqUp8xfqcTAx-lBdgpoizIaonrFfsW1E91myb426APzmjJbZWkqzUn0MpkZW34Bm-6C6qGv0JjL1s_cJO_Vx) at the Inter-university Consortium for Political and Social Research (ICPSR).
    

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)

# Resource URL: https://developers.facebook.com/docs/content-library-api/citations
Citations
=========

Each release of each product has a registered Digital Object Identifier (DOI) included in the citation formats we provide on this page. It is important that you cite the product(s) and Meta when using our data.

Meta Content Library API version v2.0
-------------------------------------

### Citation format

Meta Platforms, Inc., (Month Accessed, Year Accessed). Meta Content Library API version v2.0 [https://doi.org/10.48680/meta.metacontentlibraryapi.2.0](https://l.facebook.com/l.php?u=https%3A%2F%2Fdoi.org%2F10.48680%2Fmeta.metacontentlibraryapi.2.0&h=AT3-BJE937n9rHKRLXOEdTLIpMzcTdu7OzIjWKqwwyntwBmVycyIdWUoR6ocFTXDJUb7Fume16a86QLJpKugMkqq4ZOHxQJvi-gVUKUet6oN9RQolVvoJW3QhXtPNQiCgSE3uJbUjHZSQ9MU).

### Abstract

**Meta Content Library API** is an API for querying and analyzing Meta's full historical public content archive, supporting data analysis in Python and R in the Meta Researcher Platform, a secure digital clean room.

### Keywords

Meta, Facebook, Instagram, social media, Facebook Pages, Facebook groups, Facebook events, Facebook posts, Instagram accounts, Instagram posts, Instagram creator accounts, Instagram business accounts, Instagram personal accounts, reels

### Product limitations

Please see:

* [Search quality approach](https://developers.facebook.com/docs/content-library-api/search-quality)
    
* [Frequently asked questions](https://developers.facebook.com/docs/content-library-api/disclosures)
    

Meta Content Library version v2.0
---------------------------------

### Citation format

Meta Platforms, Inc., (Month Accessed, Year Accessed). Meta Content Library version v2.0 [https://doi.org/10.48680/meta.metacontentlibrary.2.0](https://l.facebook.com/l.php?u=https%3A%2F%2Fdoi.org%2F10.48680%2Fmeta.metacontentlibrary.2.0&h=AT3tROKdDrOYLjMHP0rHVRViIS2accCnnjr9m4jzPlCs2up9pRAI1b4P6m1fZt8L0Dx4RQe4DV2odOVQZl1WyAAZJm4ZGHMssi37cjl5f_04SnRYwQwSS4SsMo8hPPp3Um2Xs5KOAIhe6qwf).

### Abstract

**Meta Content Library** is a web-based tool that allows researchers to explore and understand data across Facebook and Instagram by offering a comprehensive, visual, searchable collection of publicly accessible content.

### Keywords

Meta, Facebook, Instagram, social media, Facebook Pages, Facebook groups, Facebook events, Instagram accounts, Instagram posts, Instagram creator accounts, Instagram business accounts, Instagram personal accounts, reels

### Product limitations

Please see:

* [Search quality approach](https://developers.facebook.com/docs/content-library-api/search-quality)
    
* [Frequently asked questions](https://developers.facebook.com/docs/content-library-api/disclosures)
    

Citations for earlier releases
------------------------------

The citation formats in the following table pertain to earlier releases of Meta Content Library and API, and are provided here for reference in reverse chronological order.

| Product and version | Citation format | Notes |
| --- | --- | --- |
| Meta Content Library API version v1.0 | Meta Platforms, Inc., (Month Accessed, Year Accessed). Meta Content Library API version v1.0 [https://doi.org/10.48680/meta.metacontentlibraryapi.1.0](https://l.facebook.com/l.php?u=https%3A%2F%2Fdoi.org%2F10.48680%2Fmeta.metacontentlibraryapi.1.0&h=AT1osVbIbJM8M0JcZKyxoLQ6GMAo8YPk4CKRqKLuBjIF5RWO1zemUXHMpvnCr4_-vyEZOCcH3GPWwXP8juNGeced8QDuuLwdIRyMK1nhys53gxaj1pYwaG-7k9EZnFCVD6cPHXRmlFP1ITzKCjWne8_7-CWDYw) | Replaced by ver. 2.0 on 1/30/2024 |
| Meta Content Library version v1.0 | Meta Platforms, Inc., (Month Accessed, Year Accessed). Meta Content Library version v1.0 [https://doi.org/10.48680/meta.metacontentlibrary.1.0](https://l.facebook.com/l.php?u=https%3A%2F%2Fdoi.org%2F10.48680%2Fmeta.metacontentlibrary.1.0&h=AT2ceerYKaR-cR3iVeiG_Rxe3LXbPRdC4PendvGxUrIZZvx_Uy2RCkXf-mOsQnBYox5tIzrc5z1Ybxlo5NSVdymdmpVGe8g2AG38f8vyTA8SaO2nFO-sGyR7MNC0VuphyaKeqWZLGOBXphEM) | Replaced by ver. 2.0 on 1/30/2024 |
| Meta Content Library API beta version v1.0 | Meta Platforms, Inc., (Month Accessed, Year Accessed). Meta Content Library API Beta version v1.0 [https://doi.org/10.48680/meta.metacontentlibraryapibetaversionv1.0](https://l.facebook.com/l.php?u=https%3A%2F%2Fdoi.org%2F10.48680%2Fmeta.metacontentlibraryapibetaversionv1.0&h=AT1s7hYrJI3jDE_xCWdgFoxuCOsR6KwuJWQMh-xA2i9Ik4rGST7BAg5IY-QfdgpzSzoTqgNt_xUyKdlf4Dlc4fVtC-mucvV66LN3H3pMZF_VjasugKz6-6-h_5_2LMsn1WD_KtQ9P__7X-q5) | Replaced by ver. 1.0 on 12/15/2023 |
| Meta Content Library beta version v1.0 | Meta Platforms, Inc., (Month Accessed, Year Accessed). Meta Content Library Beta version v1.0 [https://doi.org/10.48680/meta.metacontentlibrarybetaversionv1.0](https://l.facebook.com/l.php?u=https%3A%2F%2Fdoi.org%2F10.48680%2Fmeta.metacontentlibrarybetaversionv1.0&h=AT30qzIsUjuxjP8qhOVd5_tBoUKG15b-gnjL-vF7UwUe8fMPPgw1cGZXh8dXwoSMxTJ5wqIukjfgaTETxDp6fFhrMuczhsckoaVQxM7rISYoggzU2JoOo6E4O1uurdj3S8WdpWPXOUmffoYt) | Replaced by ver. 1.0 on 12/15/2023 |
| Researcher API early beta 0.6 | Data from Facebook Open Research and Transparency Team Researcher API 0.6, data points from all public Facebook Pages, groups, events, and post-level Facebook data from the US and select EU countries [https://doi.org/10.48680/meta.researcherapi.0.6](https://l.facebook.com/l.php?u=https%3A%2F%2Fdoi.org%2F10.48680%2Fmeta.researcherapi.0.6&h=AT3tJlHzY8pQdTXoQTDAueDn_CpyUoa7u5dZstdbSXAAStPwz9ERc3F3Zj0s_t_4IVTsYVqTWRoEPl1jkhyO_fv9FdrtSmozDTsFWYO6XUsyOCr69gKNfmlfQjWFGBUX0DfmoDbG79BblpjN) | This precursor product will be deprecated as of 1/31/2024 |

![](https://www.facebook.com/tr?id=675141479195042&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=574561515946252&ev=PageView&noscript=1)

![](https://www.facebook.com/tr?id=1754628768090156&ev=PageView&noscript=1)