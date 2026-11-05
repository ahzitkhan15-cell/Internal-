# REMEMBERED - VELTRIX TIRE SOURCE FILE PIPELINE

This file is pinned as long-term memory for this project.

## PIPELINE ORDER (DO NOT CHANGE)

1. **INGEST** - src/app.ts + src/server.ts
   - bootstrap(), createApp(), healthCheck()

2. **AUTH** - src/middlewares/auth.ts + src/routes/auth.routes.ts
   - protect(), authorize(), register(), login(), hashPassword()

3. **RATE_LIMIT** - src/middlewares/rateLimiter.ts + errorHandler.ts
   - rateLimiter (200/15min), errorHandler()

4. **VALIDATE** - src/validators/tire.validator.ts
   - createTireSchema, tireQuerySchema (Zod)

5. **ROUTE** - src/routes/*.ts
   - tireRoutes, orderRoutes, authRoutes

6. **CONTROLLER** - src/controllers/tire.controller.ts
   - getTires, getTire, createTire, updateTire, deleteTire

7. **SERVICE** - src/services/tire.service.ts [CORE]
   - findAll, findById, create, update, delete, searchByVehicle

8. **PERSIST** - src/config/database.ts + prisma/schema.prisma
   - connectDB(), Tire, User, Order, OrderItem

9. **META OBJECT** - meta.object.json + src/config/meta.ts
   - VELTRIX_META, PIPELINE_ORDER, TireMetaObject

10. **RESPONSE / OBSERVE** - src/utils/apiResponse.ts + logger.ts
   - successResponse(), paginate(), logger

## FLOW
CLIENT -> INGEST -> AUTH -> RATE_LIMIT -> VALIDATE -> ROUTE -> CONTROLLER -> SERVICE -> PERSIST -> META -> RESPONSE

STATUS: REMEMBERED ✅
DATE: 2026-05-13 (project context)
