from django.shortcuts import render
from .models import Product, Purchase
import pandas as pd

# Create your views here.

def chart_select_view(request):
    error_message = None
    df = None

    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    product_df['product_id'] = product_df['id']
    
    # print(product_df)
    # qs2 = Product.objects.all().values_list() - value list provides tuples.
    if purchase_df.shape[0] > 0:
        df = pd.merge(purchase_df, product_df, on='product_id').drop(['id_y','date_y'], axis=1).rename({'id_x': 'id', 'date_x': 'date'}, axis=1)
        if request.method == 'POST':
            # print(request.POST)
            chart_type = request.POST['sales']
            date_from = request.POST['date_from']
            date_to = request.POST.get('date_to')
            # print(chart_type,"\n",date_from,date_to)
            df['date'] = df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
            df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')

            if chart_type != "":
                if date_from != "" and date_to != "":
                    df = df[(df['date'] > date_from) & (df['date'] < date_to)]
                    df2 = df.groupby('date', as_index=False)['total_price'].agg('sum')
                # write a chart function
            else:
                error_message = "Please provide chart_type to continue"
    else:
        error_message = 'No purchase records in the database'

    context = {
        'error_message': error_message,
        # 'purchase_df': purchase_df.to_html() 
    }
    return render(request, 'products/main.html', context)
