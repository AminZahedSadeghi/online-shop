from products.models import Product

class Cart:
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')
        
        if not cart:
            cart = self.session['cart'] = {}
        
        self.cart = cart
        
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        cart = self.cart.copy()
        
        for prodcut in products:
            cart[str(prodcut.id)]['product_obj'] = prodcut
        
        for item in cart.values():
            yield item
        
    def __len__(self):
        return len(self.cart.keys())
            
        
    def add(self, product, qty=1):  # qty => quantity
        """
        Add the specified product to the cart if it exists
        """
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] =  {'qty': qty}
        else:
            self.cart[product_id]['qty'] += qty
        
        self.save()
        
    def remove(self, product):
        """
        Remove a product from the cart
        """
        product_id = str(product.id)
        
        # Check product is exists and then remove
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
            
    def clear(self):
        """
        Clear the cart
        """
        del self.session['cart']
        self.save()
        
    def total_price(self):
        """
        Return total price of cart
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        return sum([product.price*product_ids[product.id]['qty'] for product in products])

    def save(self):
        """
        Save changes in the cart
        """
        self.session.modified = True