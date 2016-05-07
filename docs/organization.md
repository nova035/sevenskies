

Backend Documentation
=====================

Support Models
--------------


### Contact Type
To retrieve all, send `GET` to `http://host:port/api/v1/common/contact_types/`

 **Payload**

    [
        {
            "id": 1,
            "name": "Phone",
            "description": null
        },
        {
            "id": 2,
            "name": "Email",
            "description": null
        },
        {
            "id": 3,
            "name": "Address",
            "description": null
        }
    ]

**Note** Rarely will you need to retrieve a contact. The 3 main types (Phone, Email & Address) used in this project have alreadly been loaded.

To retrieve one, send  `GET` to `http://host:port/api/v1/common/contact_types/<id>/`

 **Payload**

    {
        "id": 1,
        "name": "Phone",
        "description": null
    }



### Contact
To retrieve all, send `GET` to `http://host:port/api/v1/common/contacts/`

 **Payload**

    [
        {
            "id": 1,
            "contact_type_name": "Phone",
            "contact": "0716251663",
            "contact_type": 1
        },
        {
            "id": 2,
            "contact_type_name": "Email",
            "contact": "info@palvac.co.ke",
            "contact_type": 2
        },
        {
            "id": 3,
            "contact_type_name": "Address",
            "contact": "Box 1 - 90106 Nairobi",
            "contact_type": 3
        }
        ...
    ]

**Note** Rarely will you need to retrieve a contact, as contacts are usually retrieved together with the associated
oweners i.e. user, organization etc.

To retrieve one, send  `GET` to `http://host:port/api/v1/common/contacts/<id>/`

 **Payload**

    {
        "id": 1,
        "contact_type_name": "Phone",
        "contact": "0716251663",
        "contact_type": 1
    }


To create one, send  `POST` to `http://host:port/api/v1/common/locations/`

 **Payload**

    {
        "contact": "0716251663",
        "contact_type": 1
    }


### Location
To retrieve all, send `GET` to `http://host:port/api/v1/common/locations/`

 **Payload**

    [
        {
            "id": 1,
            "name": "Nairobi",
            "type": "Town"
        },
        {
            "id": 2,
            "name": "Nyeri",
           "type": "Town"
        },
        ...
    ]

To retrieve one, send  `GET` to `http://host:port/api/v1/common/locations/<id>/`

 **Payload**

    {
        "id": 1,
        "name": "Nairobi",
        "type": "Town"
    }


To create one, send  `POST` to `http://host:port/api/v1/common/locations/`

 **Payload**

    {
        "id": 1,
        "name": "Nairobi",
        "type": "Town"
    }


### Industry
To retrieve all, send `GET` to `http://host:port/api/v1/common/industries/`

 **Payload**

    [
        {
            "id": 1,
            "name": "Education"
        },
        {
            "id": 2,
            "name": "IT"
        },
        ...
    ]

To retrieve one, send  `GET` to `http://host:port/api/v1/common/industries/<id>/`

 **Payload**

    {
        "id": 1,
        "name": "Education"
    }


To create one, send  `POST` to `http://host:port/api/v1/common/industries/`

 **Payload**

    {
        "id": 1,
        "name": "Education"
    }


Functional Models
--------------

### Organization
Organization needs the following support models

- Location
- Industry

To retrieve all, send `GET` to `http://host:port/api/v1/organizations/`

 **Payload**

    [
        {
            "id": 1,
            "contacts": [
                {
                    "id": 3,
                    "contact_type_name": "Phone",
                    "contact": "0714767990",
                    "contact_type": 1
                },
                {
                    "id": 4,
                    "contact_type_name": "Email",
                    "contact": "support@yitchouse.inc.io",
                    "contact_type": 2
                },
                {
                    "id": 9,
                    "contact_type_name": "Address",
                    "contact": "Box 80100-83931, Mombasa, White House, Moi Avenue",
                    "contact_type": 3
                }
            ],
            "location_name": "Mombasa",
            "industry_name": "IT",
            "name": "Yitchouse",
            "description": "This is an IT company specialized with developing software inline with financial industry. FromERPs to Accounting specific software",
            "created": "2016-01-16T06:26:44.797335Z",
            "is_active": true,
            "logo_url": null,
            "industry": 1,
            "location": 7
        },
        {
            "id": 2,
            "contacts": [
                {
                    "id": 1,
                    "contact_type_name": "Phone",
                    "contact": "0716251663",
                    "contact_type": 1
                },
                {
                    "id": 2,
                    "contact_type_name": "Email",
                    "contact": "info@palvac.co.ke",
                    "contact_type": 2
                },
                {
                    "id": 10,
                    "contact_type_name": "Address",
                    "contact": "P.O.Box 1 - 90106 Nairobi",
                    "contact_type": 3
                }
            ],
            "location_name": "Nairobi",
            "industry_name": "Import/Export",
            "name": "Palvac Group Limited",
            "description": "Palvac Group Limited is a general import and export company. The company was formed mainly to equip Kenyans with the necessary skills so as to be able to export services to other countries in Africa, and the World. This would effectively put Kenya's Balance of Payments in a good position",
            "created": "2016-01-16T06:26:44.800023Z",
            "is_active": true,
            "logo_url": null,
            "industry": 6,
            "location": 1
        }
        ...
    ]

To retrieve one, send  `GET` to `http://host:port/api/v1/organizations/<id>/`

 **Payload**

    {
        "id": 1,
        "contacts": [
            {
                "id": 3,
                "contact_type_name": "Phone",
                "contact": "0714767990",
                "contact_type": 1
            },
            {
                "id": 4,
                "contact_type_name": "Email",
                "contact": "support@yitchouse.inc.io",
                "contact_type": 2
            },
            {
                "id": 9,
                "contact_type_name": "Address",
                "contact": "Box 80100-83931, Mombasa, White House, Moi Avenue",
                "contact_type": 3
            }
        ],
        "location_name": "Mombasa",
        "industry_name": "IT",
        "name": "Yitchouse",
        "description": "This is an IT company specialized with developing software inline with financial industry. FromERPs to Accounting specific software",
        "created": "2016-01-16T06:26:44.797335Z",
        "is_active": true,
        "logo_url": null,
        "industry": 1,
        "location": 7
    }


To create one, send  `POST` to `http://host:port/api/v1/organizations/`

 **Payload**

    {
        "name": "Palvac Group Limited", //Name of Organization
        "description": "Palvac Group Limited is a ...", //Brief summary
        "industry": 6, //ID of industry.
        "location": 1 //ID of location.
    }


### TODO - Associate an organization with a user
