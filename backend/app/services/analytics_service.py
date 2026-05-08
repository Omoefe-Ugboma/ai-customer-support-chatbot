from sqlalchemy.orm import Session

from sqlalchemy import func

from app.models.analytics import Analytics


# =========================
# LOG INTERACTION
# =========================
def log_interaction(
    db: Session,
    user_email: str,
    question: str,
    response: str,
    response_time: float,
    category: str = "general",
):

    try:

        analytics = Analytics(

            user_email=user_email,

            question=question,

            response=response,

            response_time=float(
                response_time
            ),

            category=category,
        )

        db.add(analytics)

        db.commit()

        db.refresh(analytics)

        return analytics

    except Exception as e:

        db.rollback()

        print(
            f"Analytics error: {str(e)}"
        )

        return None


# =========================
# SUMMARY
# =========================
def get_summary(
    db: Session,
    user_email: str,
):

    try:

        # =========================
        # TOTAL REQUESTS
        # =========================
        total_requests = (
            db.query(Analytics)
            .filter(
                Analytics.user_email
                == user_email
            )
            .count()
        )

        # =========================
        # AVERAGE RESPONSE TIME
        # =========================
        avg_response_time = (
            db.query(
                func.avg(
                    Analytics.response_time
                )
            )
            .filter(
                Analytics.user_email
                == user_email
            )
            .scalar()
        )

        if avg_response_time is None:

            avg_response_time = 0

        # =========================
        # CATEGORY BREAKDOWN
        # =========================
        category_data = (
            db.query(

                Analytics.category,

                func.count(
                    Analytics.id
                ),
            )
            .filter(
                Analytics.user_email
                == user_email
            )
            .group_by(
                Analytics.category
            )
            .all()
        )

        return {

            "total_requests":
                total_requests,

            "avg_response_time":
                round(
                    float(
                        avg_response_time
                    ),
                    2,
                ),

            "categories": [

                {
                    "category": cat,
                    "count": count,
                }

                for cat, count
                in category_data
            ],
        }

    except Exception as e:

        print(
            f"Summary error: {str(e)}"
        )

        return {

            "total_requests": 0,

            "avg_response_time": 0,

            "categories": [],
        }


# =========================
# RECENT ACTIVITY
# =========================
def get_recent(
    db: Session,
    user_email: str,
    limit: int = 10,
):

    try:

        records = (

            db.query(Analytics)

            .filter(
                Analytics.user_email
                == user_email
            )

            .order_by(
                Analytics.created_at.desc()
            )

            .limit(limit)

            .all()
        )

        return [

            {
                "id": r.id,

                "question":
                    r.question,

                "response":
                    r.response,

                "response_time":
                    round(
                        float(
                            r.response_time
                        ),
                        2,
                    ),

                "category":
                    r.category,

                "created_at":
                    r.created_at,
            }

            for r in records
        ]

    except Exception as e:

        print(
            f"Recent analytics error: {str(e)}"
        )

        return []