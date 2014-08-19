Send automated SMS from your web application and android phone
==============================================================

Free web api service provided courtsey: http://www.makemymails.com
To use this library you have to signup for a free web account on makemymails.com.
Your makemymails account will generate an API key for you that you can use with
this library to send sms that is automatically routed via your android phone.

Quickstart
==========

Getting setup (one time)
------------------------

* Sign up on Makemymails `[1]`_ and note your username somewhere

* Install Makemymails Android App `[2]_` and enter MMM username you used to register on the makemymails website.
  (Press "Associate username" button to associate your device with Makemymails web account)

* Visit http://www.makemymails.com/sms/api-details/ `[3]_`
  This page contains the MMM_API_KEY which can be used with this library.
  Please  note it at a safe place and do not share it with anyone as the key
  is unique to you.


Steps with illustrations are available in this doc:


Sending sms from python code
----------------------------

You can use import the *sendsms* function from makemymails after installing this package.

.. code-block:: python

    MMM_API_KEY = 'AJK7G5J2KL6JGJU7'    # A unique API key is provided to you with
                                        # your Makemymails account. Keep this key safe.
    DEVICE_ID = '18'            # A unique device id is assigned to each of your
                                # device associated with your makemymails web account
                                # You can see devide id for all id's the api details page above.
    receiver = '9876534210'
    msg = 'This is a test sms from Makemymails SMS free API'
    from makemymails import sendsms
    sendsms(send_to=receiver, sms_body=msg, MMM_API_KEY, DEVICE_ID)


Requirements
-------------

- Android Phone must be connected to internet at all times
- Sim on the android phone for sending messages.


Warning
-------
Warning: Api calls you make cause sms to be sent via your android phone,
please make sure you install an sms pack before sending sms.


.. _[1]: http://www.makemymails.com/accounts/signup/
.. _[2]: https://play.google.com/store/apps/details?id=awsms.mmm
.. _[3]: http://www.makemymails.com/sms/api-details/
