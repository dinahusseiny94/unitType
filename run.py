import pandas as pd

lookup = pd.read_excel('/Users/dinaelhusseiny/Desktop/Ba7i/Gen units.xlsx')
dataset = pd.read_excel('/Users/dinaelhusseiny/Desktop/Ba7i/bids1-09-2020.xlsx')

merged = pd.merge(left=dataset, right=lookup, how='left', left_on='unidad', right_on=' Unid.Prog. ')
merged = merged[['hora', 'fecha', 'pais', 'unidad', 'tipo_oferta',
                'energía_compra_venta', 'precio_compra_venta', 'ofertada_o_casada_c',
                'Filter', ' Tipo ']]
merged.to_excel('/Users/dinaelhusseiny/Desktop/Ba7i/merged_output.xlsx', encoding='utf-8-sig', index=False)

