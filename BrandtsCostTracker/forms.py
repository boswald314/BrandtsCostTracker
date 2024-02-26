from django import forms

class UploadInvoiceForm(forms.Form):
    image = forms.ImageField(
        label='Select an invoice image to upload',
        help_text='Max. 42 megabytes'
    )

# If you have other forms that require input for the price history, you can define them here.
# For example, to add an item and its price history, you might use:

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item  # Assuming 'Item' is the name of your model
        fields = ['name', 'supplier', 'case_size', 'quantity_ordered']

class PriceHistoryForm(forms.ModelForm):
    class Meta:
        model = PriceHistory
        fields = ['product', 'price', 'date', 'invoice_image']
