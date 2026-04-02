from django.contrib import admin
from .models import Product, Review, Store, ProductDetail


class ReviewInline(admin.TabularInline):
	model = Review
	extra = 2


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'status', 'created_at')
	list_filter = ('status', 'created_at')
	search_fields = ('name', 'description')
	inlines = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	list_display = ('product', 'user', 'rating', 'created_at')
	list_filter = ('rating', 'created_at')
	search_fields = ('product__name', 'user__username', 'review')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
	list_display = ('name',)
	search_fields = ('name',)


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
	list_display = ('product', 'details')
	search_fields = ('product__name',)
