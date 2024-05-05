product = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "payload": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "object",
                    "properties": {
                        "id": {
                            "type": "integer"
                        },
                        "title": {
                            "type": "string"
                        },
                        "category": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "productAmount": {
                                    "type": "integer"
                                },
                                "parent": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "productAmount": {
                                            "type": "integer"
                                        },
                                        "parent": {
                                            "type": "object",
                                            "properties": {
                                                "id": {
                                                    "type": "integer"
                                                },
                                                "title": {
                                                    "type": "string"
                                                },
                                                "productAmount": {
                                                    "type": "integer"
                                                },
                                                "parent": {
                                                    "type": "null"
                                                }
                                            },
                                            "required": [
                                                "id",
                                                "title",
                                                "productAmount",
                                                "parent"
                                            ]
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "productAmount",
                                        "parent"
                                    ]
                                }
                            },
                            "required": [
                                "id",
                                "title",
                                "productAmount",
                                "parent"
                            ]
                        },
                        "rating": {
                            "type": "number"
                        },
                        "reviewsAmount": {
                            "type": "integer"
                        },
                        "ordersAmount": {
                            "type": "integer"
                        },
                        "rOrdersAmount": {
                            "type": "integer"
                        },
                        "totalAvailableAmount": {
                            "type": "integer"
                        },
                        "charityCommission": {
                            "type": "integer"
                        },
                        "description": {
                            "type": "string"
                        },
                        "comments": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "commentType": {
                                            "type": "string"
                                        },
                                        "comment": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "commentType",
                                        "comment"
                                    ]
                                }
                            ]
                        },
                        "attributes": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                },
                                {
                                    "type": "string"
                                }
                            ]
                        },
                        "tags": {
                            "type": "array",
                            "items": {}
                        },
                        "synonyms": {
                            "type": "array",
                            "items": {}
                        },
                        "photos": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "photo": {
                                            "type": "object",
                                            "properties": {
                                                "800": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                },
                                                "720": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                },
                                                "480": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                },
                                                "240": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                },
                                                "80": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                },
                                                "24034": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                },
                                                "120": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                },
                                                "540": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                },
                                                "60": {
                                                    "type": "object",
                                                    "properties": {
                                                        "high": {
                                                            "type": "string"
                                                        },
                                                        "low": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "high",
                                                        "low"
                                                    ]
                                                }
                                            },
                                            "required": [
                                                "800",
                                                "720",
                                                "480",
                                                "240",
                                                "80",
                                                "24034",
                                                "120",
                                                "540",
                                                "60"
                                            ]
                                        },
                                        "photoKey": {
                                            "type": "string"
                                        },
                                        "color": {
                                            "type": "null"
                                        },
                                        "hasVerticalPhoto": {
                                            "type": "boolean"
                                        }
                                    },
                                    "required": [
                                        "photo",
                                        "photoKey",
                                        "color",
                                        "hasVerticalPhoto"
                                    ]
                                }
                            ]
                        },
                        "video": {
                            "type": "null"
                        },
                        "hasCircularPhotos": {
                            "type": "boolean"
                        },
                        "circularPhotosList": {
                            "type": "array",
                            "items": {}
                        },
                        "characteristics": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "title": {
                                            "type": "string"
                                        },
                                        "values": {
                                            "type": "array",
                                            "items": [
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {
                                                            "type": "integer"
                                                        },
                                                        "title": {
                                                            "type": "string"
                                                        },
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "title",
                                                        "value"
                                                    ]
                                                },
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {
                                                            "type": "integer"
                                                        },
                                                        "title": {
                                                            "type": "string"
                                                        },
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "title",
                                                        "value"
                                                    ]
                                                },
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {
                                                            "type": "integer"
                                                        },
                                                        "title": {
                                                            "type": "string"
                                                        },
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "title",
                                                        "value"
                                                    ]
                                                },
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {
                                                            "type": "integer"
                                                        },
                                                        "title": {
                                                            "type": "string"
                                                        },
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "title",
                                                        "value"
                                                    ]
                                                },
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "id": {
                                                            "type": "integer"
                                                        },
                                                        "title": {
                                                            "type": "string"
                                                        },
                                                        "value": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "id",
                                                        "title",
                                                        "value"
                                                    ]
                                                }
                                            ]
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "title",
                                        "values"
                                    ]
                                }
                            ]
                        },
                        "productOptionDtos": {
                            "type": "array",
                            "items": {}
                        },
                        "skuList": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "characteristics": {
                                            "type": "array",
                                            "items": [
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "charIndex": {
                                                            "type": "integer"
                                                        },
                                                        "valueIndex": {
                                                            "type": "integer"
                                                        }
                                                    },
                                                    "required": [
                                                        "charIndex",
                                                        "valueIndex"
                                                    ]
                                                }
                                            ]
                                        },
                                        "availableAmount": {
                                            "type": "integer"
                                        },
                                        "fullPrice": {
                                            "type": "number"
                                        },
                                        "charityProfit": {
                                            "type": "number"
                                        },
                                        "purchasePrice": {
                                            "type": "number"
                                        },
                                        "barcode": {
                                            "type": "integer"
                                        },
                                        "address": {
                                            "type": "null"
                                        },
                                        "dimension": {
                                            "type": "object",
                                            "properties": {
                                                "length": {
                                                    "type": "integer"
                                                },
                                                "width": {
                                                    "type": "integer"
                                                },
                                                "height": {
                                                    "type": "integer"
                                                },
                                                "weight": {
                                                    "type": "integer"
                                                }
                                            },
                                            "required": [
                                                "length",
                                                "width",
                                                "height",
                                                "weight"
                                            ]
                                        },
                                        "offer": {
                                            "type": "null"
                                        },
                                        "discountBadge": {
                                            "type": "null"
                                        },
                                        "installment": {
                                            "type": "null"
                                        },
                                        "productOptionDtos": {
                                            "type": "array",
                                            "items": [
                                                {
                                                    "type": "object",
                                                    "properties": {
                                                        "optionId": {
                                                            "type": "integer"
                                                        },
                                                        "text": {
                                                            "type": "string"
                                                        },
                                                        "type": {
                                                            "type": "string"
                                                        },
                                                        "paymentInfo": {
                                                            "type": "string"
                                                        },
                                                        "active": {
                                                            "type": "boolean"
                                                        },
                                                        "titleBanner": {
                                                            "type": "string"
                                                        }
                                                    },
                                                    "required": [
                                                        "optionId",
                                                        "text",
                                                        "type",
                                                        "paymentInfo",
                                                        "active",
                                                        "titleBanner"
                                                    ]
                                                }
                                            ]
                                        },
                                        "vat": {
                                            "type": "object",
                                            "properties": {
                                                "type": {
                                                    "type": "string"
                                                },
                                                "vatRate": {
                                                    "type": "integer"
                                                },
                                                "vatAmount": {
                                                    "type": "number"
                                                },
                                                "price": {
                                                    "type": "number"
                                                }
                                            },
                                            "required": [
                                                "type",
                                                "vatRate",
                                                "vatAmount",
                                                "price"
                                            ]
                                        },
                                        "circularPhotosList": {
                                            "type": "array",
                                            "items": {}
                                        },
                                        "videoUrl": {
                                            "type": "null"
                                        },
                                        "sellPrice": {
                                            "type": "integer"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "characteristics",
                                        "availableAmount",
                                        "fullPrice",
                                        "charityProfit",
                                        "purchasePrice",
                                        "barcode",
                                        "address",
                                        "dimension",
                                        "offer",
                                        "discountBadge",
                                        "installment",
                                        "productOptionDtos",
                                        "vat",
                                        "circularPhotosList",
                                        "videoUrl",
                                        "sellPrice"
                                    ]
                                }
                            ]
                        },
                        "seller": {
                            "type": "object",
                            "properties": {
                                "id": {
                                    "type": "integer"
                                },
                                "title": {
                                    "type": "string"
                                },
                                "link": {
                                    "type": "string"
                                },
                                "banner": {
                                    "type": "null"
                                },
                                "avatar": {
                                    "type": "null"
                                },
                                "description": {
                                    "type": "string"
                                },
                                "hasCharityProducts": {
                                    "type": "boolean"
                                },
                                "registrationDate": {
                                    "type": "integer"
                                },
                                "rating": {
                                    "type": "number"
                                },
                                "reviews": {
                                    "type": "integer"
                                },
                                "orders": {
                                    "type": "integer"
                                },
                                "official": {
                                    "type": "boolean"
                                },
                                "contacts": {
                                    "type": "array",
                                    "items": {}
                                },
                                "categories": {
                                    "type": "array",
                                    "items": {}
                                },
                                "currentCategory": {
                                    "type": "null"
                                },
                                "filters": {
                                    "type": "array",
                                    "items": {}
                                },
                                "appliedFilters": {
                                    "type": "array",
                                    "items": {}
                                },
                                "priceFilter": {
                                    "type": "null"
                                },
                                "totalProducts": {
                                    "type": "integer"
                                },
                                "parents": {
                                    "type": "array",
                                    "items": {}
                                },
                                "products": {
                                    "type": "array",
                                    "items": {}
                                },
                                "sellerAccountId": {
                                    "type": "integer"
                                },
                                "info": {
                                    "type": "null"
                                }
                            },
                            "required": [
                                "id",
                                "title",
                                "link",
                                "banner",
                                "avatar",
                                "description",
                                "hasCharityProducts",
                                "registrationDate",
                                "rating",
                                "reviews",
                                "orders",
                                "official",
                                "contacts",
                                "categories",
                                "currentCategory",
                                "filters",
                                "appliedFilters",
                                "priceFilter",
                                "totalProducts",
                                "parents",
                                "products",
                                "sellerAccountId",
                                "info"
                            ]
                        },
                        "topFeedback": {
                            "type": "object",
                            "properties": {
                                "reviewId": {
                                    "type": "integer"
                                },
                                "productId": {
                                    "type": "integer"
                                },
                                "date": {
                                    "type": "integer"
                                },
                                "edited": {
                                    "type": "boolean"
                                },
                                "customer": {
                                    "type": "string"
                                },
                                "reply": {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "date": {
                                            "type": "integer"
                                        },
                                        "edited": {
                                            "type": "boolean"
                                        },
                                        "content": {
                                            "type": "string"
                                        },
                                        "shop": {
                                            "type": "string"
                                        },
                                        "photos": {
                                            "type": "array",
                                            "items": {}
                                        },
                                        "liked": {
                                            "type": "null"
                                        },
                                        "disliked": {
                                            "type": "null"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "date",
                                        "edited",
                                        "content",
                                        "shop",
                                        "photos",
                                        "liked",
                                        "disliked"
                                    ]
                                },
                                "rating": {
                                    "type": "integer"
                                },
                                "characteristics": {
                                    "type": "array",
                                    "items": [
                                        {
                                            "type": "object",
                                            "properties": {
                                                "characteristic": {
                                                    "type": "string"
                                                },
                                                "characteristicValue": {
                                                    "type": "string"
                                                }
                                            },
                                            "required": [
                                                "characteristic",
                                                "characteristicValue"
                                            ]
                                        }
                                    ]
                                },
                                "pros": {
                                    "type": "null"
                                },
                                "cons": {
                                    "type": "null"
                                },
                                "content": {
                                    "type": "string"
                                },
                                "photos": {
                                    "type": "array",
                                    "items": {}
                                },
                                "status": {
                                    "type": "string"
                                },
                                "hasVerticalPhoto": {
                                    "type": "null"
                                },
                                "like": {
                                    "type": "boolean"
                                },
                                "dislike": {
                                    "type": "boolean"
                                },
                                "amountLike": {
                                    "type": "integer"
                                },
                                "amountDislike": {
                                    "type": "integer"
                                },
                                "id": {
                                    "type": "integer"
                                },
                                "isAnonymous": {
                                    "type": "boolean"
                                }
                            },
                            "required": [
                                "reviewId",
                                "productId",
                                "date",
                                "edited",
                                "customer",
                                "reply",
                                "rating",
                                "characteristics",
                                "pros",
                                "cons",
                                "content",
                                "photos",
                                "status",
                                "hasVerticalPhoto",
                                "like",
                                "dislike",
                                "amountLike",
                                "amountDislike",
                                "id",
                                "isAnonymous"
                            ]
                        },
                        "isEco": {
                            "type": "boolean"
                        },
                        "isPerishable": {
                            "type": "boolean"
                        },
                        "hasVerticalPhoto": {
                            "type": "boolean"
                        },
                        "showKitty": {
                            "type": "boolean"
                        },
                        "bonusProduct": {
                            "type": "boolean"
                        },
                        "badges": {
                            "type": "array",
                            "items": [
                                {
                                    "type": "object",
                                    "properties": {
                                        "id": {
                                            "type": "integer"
                                        },
                                        "text": {
                                            "type": "string"
                                        },
                                        "textColor": {
                                            "type": "string"
                                        },
                                        "backgroundColor": {
                                            "type": "string"
                                        },
                                        "description": {
                                            "type": "string"
                                        },
                                        "link": {
                                            "type": "null"
                                        },
                                        "type": {
                                            "type": "string"
                                        }
                                    },
                                    "required": [
                                        "id",
                                        "text",
                                        "textColor",
                                        "backgroundColor",
                                        "description",
                                        "link",
                                        "type"
                                    ]
                                }
                            ]
                        },
                        "volumeDiscount": {
                            "type": "null"
                        },
                        "favourite": {
                            "type": "boolean"
                        },
                        "colorPhotoPreview": {
                            "type": "boolean"
                        },
                        "adultCategory": {
                            "type": "boolean"
                        }
                    },
                    "required": [
                        "id",
                        "title",
                        "category",
                        "rating",
                        "reviewsAmount",
                        "ordersAmount",
                        "rOrdersAmount",
                        "totalAvailableAmount",
                        "charityCommission",
                        "description",
                        "comments",
                        "attributes",
                        "tags",
                        "synonyms",
                        "photos",
                        "video",
                        "hasCircularPhotos",
                        "circularPhotosList",
                        "characteristics",
                        "productOptionDtos",
                        "skuList",
                        "seller",
                        "topFeedback",
                        "isEco",
                        "isPerishable",
                        "hasVerticalPhoto",
                        "showKitty",
                        "bonusProduct",
                        "badges",
                        "volumeDiscount",
                        "favourite",
                        "colorPhotoPreview",
                        "adultCategory"
                    ]
                },
                "promotion": {
                    "type": "object",
                    "properties": {
                        "actions": {
                            "type": "array",
                            "items": {}
                        }
                    },
                    "required": [
                        "actions"
                    ]
                }
            },
            "required": [
                "data",
                "promotion"
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
