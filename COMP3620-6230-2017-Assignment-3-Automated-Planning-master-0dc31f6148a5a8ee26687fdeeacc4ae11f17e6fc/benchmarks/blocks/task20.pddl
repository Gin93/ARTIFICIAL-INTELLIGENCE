(define (problem blocks-10-1)
(:domain blocks)
(:objects d a j i e g h b f c - block)
(:init (clear c) (clear f) (ontable b) (ontable h) (on c g) (on g e) (on e i)
 (on i j) (on j a) (on a b) (on f d) (on d h) (handempty))
(:goal (and (on c b) (on b d) (on d f) (on f i) (on i a) (on a e) (on e h)
            (on h g) (on g j)))
)