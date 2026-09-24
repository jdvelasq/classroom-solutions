-- La capa analítica resume la semilla sin depender de pasos manuales.

select
    factory_id,
    sum(daily_units_produced) as total_units_produced
from {{ ref('daily_operations') }}
group by factory_id
