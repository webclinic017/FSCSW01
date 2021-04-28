import runtest.run_django
from runtest.fixtures.value_set import ValueSetTuple, SetMemberTuple, load_value_sets
from runtest.fixtures.set_audit_user import set_audit_user

# Placed here so that it can be imported by testcases
# Stock code follows Yahoo Finance
stocks = [
    ValueSetTuple(value_set_code='STOCKS', value_set_description='Stocks available for backtesting',
        set_member_list=(
            SetMemberTuple(value_code='6888.KL', value_description='AXIATA', sort_order=1,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='1023.KL', value_description='CIMB', sort_order=2,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='7277.KL', value_description='DIALOG', sort_order=3,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='6947.KL', value_description='DIGI', sort_order=4,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='3182.KL', value_description='GENTING', sort_order=5,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='4715.KL', value_description='GENM', sort_order=6,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='3034.KL', value_description='HAPSENG', sort_order=7,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='5168.KL', value_description='HARTALEGA', sort_order=8,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='5819.KL', value_description='HONGLEONGBANK', sort_order=9,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='1082.KL', value_description='HONGLEONGGROUP', sort_order=10,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='5225.KL', value_description='IHH', sort_order=11,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='1961.KL', value_description='IOI', sort_order=12,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='2445.KL', value_description='KLK', sort_order=13,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='1155.KL', value_description='MAYBANK', sort_order=14,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='6012.KL', value_description='MAXIS', sort_order=15,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='3816.KL', value_description='MISC', sort_order=16,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='4707.KL', value_description='NESTLE', sort_order=17,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='5183.KL', value_description='PCHEM', sort_order=18,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='5681.KL', value_description='PDAGANG', sort_order=19,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='6033.KL', value_description='PGAS', sort_order=20,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='4065.KL', value_description='PPB', sort_order=21,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='8869.KL', value_description='PMETAL', sort_order=22,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='1295.KL', value_description='PUBLIC', sort_order=23,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='1066.KL', value_description='RHB', sort_order=24,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='4197.KL', value_description='SIMEDARBY', sort_order=25,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='5285.KL', value_description='SIMEPLANT', sort_order=26,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='7106.KL', value_description='SUPERMAX', sort_order=27,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='4863.KL', value_description='TELEKOM', sort_order=28,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='5347.KL', value_description='TENAGA', sort_order=29,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            SetMemberTuple(value_code='7113.KL', value_description='TOPGLOVE', sort_order=30,
                    param_1_code=None, param_2_code=None, param_3_code=None),
            )
        )
    ]
    

if __name__ == '__main__':
    set_audit_user()
    (ic, uc, mic, muc) = load_value_sets(stocks)
    print("Stocks: Inserted: %d, Updated: %d" % (mic, muc))
