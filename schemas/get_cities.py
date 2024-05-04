cities = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "payload": {
            "type": "array",
            "items": [
                {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "name": {
                            "type": "string"
                        },
                        "deliveryPrice": {
                            "type": "number"
                        },
                        "region": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "name": {
                                    "type": "string"
                                },
                                "code": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "id",
                                "name",
                                "code"
                            ]
                        },
                        "hasEcoDelivery": {
                            "type": "boolean"
                        },
                        "deliveryPoints": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "address": {
                                            "type": "string"
                                        },
                                        "timeFrom": {
                                            "type": "string"
                                        },
                                        "timeTo": {
                                            "type": "string"
                                        },
                                        "schedule": {
                                            "type": "object",
                                            "properties": {
                                                "days": {
                                                    "type": "array",
                                                    "items": [
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "day": {
                                                                    "type": "string"
                                                                },
                                                                "timeFrom": {
                                                                    "type": "string"
                                                                },
                                                                "timeTo": {
                                                                    "type": "string"
                                                                },
                                                                "color": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "day",
                                                                "timeFrom",
                                                                "timeTo",
                                                                "color"
                                                            ]
                                                        },
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "day": {
                                                                    "type": "string"
                                                                },
                                                                "timeFrom": {
                                                                    "type": "string"
                                                                },
                                                                "timeTo": {
                                                                    "type": "string"
                                                                },
                                                                "color": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "day",
                                                                "timeFrom",
                                                                "timeTo",
                                                                "color"
                                                            ]
                                                        },
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "day": {
                                                                    "type": "string"
                                                                },
                                                                "timeFrom": {
                                                                    "type": "string"
                                                                },
                                                                "timeTo": {
                                                                    "type": "string"
                                                                },
                                                                "color": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "day",
                                                                "timeFrom",
                                                                "timeTo",
                                                                "color"
                                                            ]
                                                        },
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "day": {
                                                                    "type": "string"
                                                                },
                                                                "timeFrom": {
                                                                    "type": "string"
                                                                },
                                                                "timeTo": {
                                                                    "type": "string"
                                                                },
                                                                "color": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "day",
                                                                "timeFrom",
                                                                "timeTo",
                                                                "color"
                                                            ]
                                                        },
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "day": {
                                                                    "type": "string"
                                                                },
                                                                "timeFrom": {
                                                                    "type": "string"
                                                                },
                                                                "timeTo": {
                                                                    "type": "string"
                                                                },
                                                                "color": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "day",
                                                                "timeFrom",
                                                                "timeTo",
                                                                "color"
                                                            ]
                                                        },
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "day": {
                                                                    "type": "string"
                                                                },
                                                                "timeFrom": {
                                                                    "type": "string"
                                                                },
                                                                "timeTo": {
                                                                    "type": "string"
                                                                },
                                                                "color": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "day",
                                                                "timeFrom",
                                                                "timeTo",
                                                                "color"
                                                            ]
                                                        },
                                                        {
                                                            "type": "object",
                                                            "properties": {
                                                                "day": {
                                                                    "type": "string"
                                                                },
                                                                "timeFrom": {
                                                                    "type": "string"
                                                                },
                                                                "timeTo": {
                                                                    "type": "string"
                                                                },
                                                                "color": {
                                                                    "type": "string"
                                                                }
                                                            },
                                                            "required": [
                                                                "day",
                                                                "timeFrom",
                                                                "timeTo",
                                                                "color"
                                                            ]
                                                        }
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "days"
                                            ]
                                        },
                                        "hasDressingRoom": {
                                            "type": "boolean"
                                        },
                                        "hasEcoEndpoint": {
                                            "type": "boolean"
                                        },
                                        "acceptReturns": {
                                            "type": "boolean"
                                        },
                                        "longitude": {
                                            "type": "number"
                                        },
                                        "latitude": {
                                            "type": "number"
                                        },
                                        "deliveryPrice": {
                                            "type": "null"
                                        },
                                        "shelfLife": {
                                            "type": "integer"
                                        },
                                        "iconAvailableUrl": {
                                            "type": "string"
                                        },
                                        "iconAvailableSelectedUrl": {
                                            "type": "string"
                                        },
                                        "iconUnavailableUrl": {
                                            "type": "string"
                                        },
                                        "iconUnavailableSelectedUrl": {
                                            "type": "string"
                                        },
                                        "name": {
                                            "type": "string"
                                        },
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "address",
                                        "timeFrom",
                                        "timeTo",
                                        "schedule",
                                        "hasDressingRoom",
                                        "hasEcoEndpoint",
                                        "acceptReturns",
                                        "longitude",
                                        "latitude",
                                        "deliveryPrice",
                                        "shelfLife",
                                        "iconAvailableUrl",
                                        "iconAvailableSelectedUrl",
                                        "iconUnavailableUrl",
                                        "iconUnavailableSelectedUrl",
                                        "name",
                                        "type"
                                    ]
                                }
                            ]
                        },
                        "keProductsDeliveryDate": {
                            "type": "null"
                        },
                        "ecoProductsDeliveryDate": {
                            "type": "null"
                        }
                    },
                    "required": [
                        "id",
                        "name",
                        "deliveryPrice",
                        "region",
                        "hasEcoDelivery",
                        "deliveryPoints",
                        "keProductsDeliveryDate",
                        "ecoProductsDeliveryDate"
                    ]
                }
            ]
        },
        "timestamp": {
            "type": "string"
        }
    },
    "required": [
        "payload",
        "timestamp"
    ]
}
